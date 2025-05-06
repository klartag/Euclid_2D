from pathlib import Path
import time
import tqdm


from ..predicates.predicate_factory import predicate_from_args
from ..geometry_objects.construction_object import ConstructionObject
from ..proof.proof import Proof
from ..proof.steps import Step, AssertStep, ObjDefineStep, TheoremStep
from ..proof_checker import ADD_CFG, ProofChecker, involved_objects
from ..geometry_trackers.geometry_tracker import unpack_predicate_minimal
from ..geometry_objects.equation_object import EquationObject
from ..proof_gen.gen_utils import is_trivial
from ..rule_utils import LITERAL, ProofCheckError, union
from ..theorem import Theorem
from util import BASE_PATH


def compute_assumption_requirement_graph(proof: Proof, step_requirements: list[set[int]], verb=False) -> list[set[int]]:
    """
    Computes an approximation of the directed acyclic graph of the requirements
    of the proof assumptions by the steps.

    Parameters:
    * `proof`: A proof in whose dependency graph we are interested.
    * `step_requirements`: The dependency graph of theorems on each other.

    Return:

    A list `res` of sets, in which `res[i]` contains the indices of the assumptions used by the step.
    """
    checker = ProofChecker(proof)
    checker.geometry_tracker.load_embeds(proof)
    for obj in proof.assumption_objects.values():
        checker.geometry_tracker.get_object(obj, ADD_CFG)

    # Initializing the array of proof-checkers without a single assumption.
    checkers: list[ProofChecker] = []
    iterator = tqdm.tqdm(enumerate(proof.assumption_predicates)) if verb else enumerate(proof.assumption_predicates)
    for idx, pred in iterator:
        skip_checker = checker.shallow_copy()

        for other_pred in proof.assumption_predicates[idx + 1 :]:
            skip_checker.geometry_tracker.add_predicate(other_pred, ADD_CFG, 'Assumption')

        checkers.append(skip_checker)
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Assumption')

    reqs = [set() for _ in proof.steps]

    # We iterate over the steps and check which steps stop working as a result of skipping each step.
    for skip_idx, checker in enumerate(checkers):
        failed_idx = set()

        for curr_idx, step in enumerate(proof.steps):
            try:
                checker.add_step(step)
            except ProofCheckError:
                if len(step_requirements[curr_idx] & failed_idx) == 0:
                    reqs[curr_idx].add(skip_idx)
                failed_idx.add(curr_idx)

    return reqs


def compute_step_requirements_graph(proof: Proof, verb=False) -> list[set[int]]:
    """
    Computes an approximation of the directed acyclic graph of the requirements between steps.
    Each step points at all previous steps that are necessary for the step to be true
    and are not necessary to any other necessary steps between the two.

    This might still miss requirements that are proved twice.
    """

    checker = ProofChecker(proof)
    checker.geometry_tracker.load_embeds(proof)
    for obj in proof.assumption_objects.values():
        checker.geometry_tracker.get_object(obj, ADD_CFG)
    for pred in proof.assumption_predicates:
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Assumption')
    for pred in proof.auxiliary_predicates:
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Auxiliary')

    # Initializing the checkers array.
    checkers: list[ProofChecker] = []
    for step in proof.steps:
        checkers.append(checker.shallow_copy())
        checker.add_step(step)

    reqs = [set() for _ in proof.steps]

    # We iterate over the steps and check which steps stop working as a result of skipping each step.
    iterator = reversed(range(len(proof.steps)))
    if tqdm:
        iterator = tqdm.tqdm(iterator)

    for skip_idx in reversed(range(len(proof.steps))):
        added_steps = set(range(skip_idx))
        curr_checker = checkers[skip_idx]

        for curr_idx, step in enumerate(proof.steps[skip_idx + 1 :]):
            curr_idx += skip_idx + 1
            try:
                curr_checker.add_step(step)
                added_steps.add(curr_idx)
            except ProofCheckError:
                if all(req in added_steps for req in reqs[curr_idx]):
                    reqs[curr_idx].add(skip_idx)

    return reqs


def compute_requirement_graph_2(proof: Proof, verb=False) -> tuple[list[set[int]], list[set[int]]]:
    """
    Computes an approximation of the directed acyclic graph of the requirements between steps.
    Each step points at all previous steps in which one of the predicates required by the step
    became known to the checker.
    This is only a subset of the true computational graph, since there may be predicates that
    are formed by a combination of some other predicates (Such as linear algebra results, or everything derived from equalities).

    In the single example I checker, the graph was too rough and innacurate to be useful.

    Parameters:
    * `proof`: The proof for which we compute the graph.
    * `verb`: Whether to print debug information.

    Return:

    A list of sets of the indices required by each step.
    """
    # Finding the requirements required by each step.
    reqs = [[] for _ in proof.steps]
    for req, step in zip(reqs, proof.steps):
        if isinstance(step, TheoremStep):
            theo = Theorem.all_theorems()[step.theorem_name]
            subs = {sig: inp for sig, inp in zip(theo.signature, step.inputs)}
            req.extend(pred.substitute(subs) for pred in theo.required_predicates)
        elif isinstance(step, ObjDefineStep):
            obj = step.right_hand if step.right_hand is not None else step.left_hand
            if not isinstance(obj, ConstructionObject):
                continue
            req.extend(obj.requirements())
        elif isinstance(step, AssertStep):
            req.extend(step.predicates)

    # Unpacking the predicates.
    reqs = [union(unpack_predicate_minimal(pred) for pred in step_reqs) for step_reqs in reqs]

    checker = ProofChecker(proof)
    checker.geometry_tracker.load_embeds(proof)
    for obj in proof.assumption_objects.values():
        checker.geometry_tracker.get_object(obj, ADD_CFG)
    assumption_requirements = [set() for _ in proof.steps]

    for pred in proof.auxiliary_predicates:
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Auxiliary')

    for idx, pred in tqdm.tqdm(enumerate(proof.assumption_predicates)):
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Assumption')

        for curr_req, curr_res in zip(reqs, assumption_requirements):
            contained_predicates = {pred for pred in curr_req if checker.geometry_tracker.contains_predicate(pred)}
            if len(contained_predicates) > 0:
                curr_res.add(idx)
                curr_req -= contained_predicates

    predicate_requirements = [set() for _ in proof.steps]
    for idx, step in tqdm.tqdm(enumerate(proof.steps)):
        checker.add_step(step)

        for curr_req, curr_res in zip(reqs[idx + 1 :], predicate_requirements[idx + 1 :]):
            contained_predicates = {pred for pred in curr_req if checker.geometry_tracker.contains_predicate(pred)}
            if len(contained_predicates) > 0:
                curr_res.add(idx)
                curr_req -= contained_predicates

    return assumption_requirements, predicate_requirements


def trim_proof(proof: Proof, *, verbose=False) -> Proof:
    """
    Greedily removes unnecessary steps from the proof.

    Parameters:
    * `proof`: The proof to trim.
    * `verbose`: Whether to print debug data on the proof trimming process.

    Return:

    A proof, where steps whose removal does not change the proof's correctness are removed.
    """

    """
    The algorithm for removing steps is as follows.
    Ideally, we would like to go from the end to the beginning, removing each step and checking if the proof still works.
    If it does, we remove the step, and otherwise we keep it.
    To not run the beginning tons of times, we store checkpoints while adding steps from the proof to the checker.
    
    To accelerate the algorithm, instead of removing a single step each time, we remove several. 
    Since usually when trimming proofs the result is far shorter than the input, 
    this can accelerate the code by a significant factor (In `test_problem_2`, it accelerated things by a factor of 5).
    In the worst case, we see that the proof is dense and don't skip at all, incurring no cost.
    """

    t0 = time.time()

    proof_objects = list(proof.assumption_objects.values())

    checker = ProofChecker(proof)
    checker_before_object: list[ProofChecker] = []

    for obj in proof_objects:
        checker_before_object.append(checker.shallow_copy())
        checker.geometry_tracker.get_object(obj, ADD_CFG)
        if obj in proof.embeds:
            for pred in checker.geometry_tracker.numeric_tracker.add_object(obj, proof.embeds[obj]):
                checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'From numeric.')

    if verbose:
        print(f'Initializing checkers... (t={time.time() - t0:.1f})')

    # Initializing the array of proof-checkers without a single assumption.
    checker_before_assumption: list[ProofChecker] = []
    for pred in proof.assumption_predicates:
        checker_before_assumption.append(checker.shallow_copy())
        checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Assumption')
    iterator: tqdm.tqdm[Step] | list[Step] = tqdm.tqdm(proof.steps, 'Processed step: ') if verbose else proof.steps
    checker_before_step: list[ProofChecker] = []
    for step in iterator:
        checker_before_step.append(checker.shallow_copy())
        checker.add_step(step)

    false_found = any(pred.name == 'false' for pred in checker.geometry_tracker.all_predicates())

    if verbose:
        print(f'Skipping steps... (t={time.time() - t0:.1f})')

    skip_steps = [True] * len(proof.steps)

    good_steps = 1

    i = len(proof.steps)
    while i > 0:
        all_steps = len(proof.steps) - i + 1

        if verbose:
            print(f'Outer loop {i=} {all_steps=} {good_steps=}')
        no_skip_prob = good_steps / all_steps
        attempt_skip = min(i, int(1 / no_skip_prob))
        low_i = i - attempt_skip
        curr_i = low_i
        failed_once = False
        while True:
            if verbose:
                print(f'Inner loop {low_i=} {curr_i=} {i=}')

            # Checking if skipping everything from curr_i to i is fine.
            success = True
            curr_checker = checker_before_step[curr_i]
            pure_geo_objects = set(curr_checker.geometry_tracker.all_objects())
            try:
                for step, can_skip_step in zip(proof.steps[i:], skip_steps[i:]):
                    # Attempting to add the step.
                    if not can_skip_step:
                        curr_checker.add_step(step)
                        if isinstance(step, TheoremStep):
                            pure_geo_objects |= set(step.result_objects)
                        elif isinstance(step, ObjDefineStep):
                            pure_geo_objects.add(step.left_hand)
                pure_geo_objects = {
                    obj
                    for obj in pure_geo_objects
                    if not isinstance(obj, ConstructionObject)
                    and not isinstance(obj, EquationObject)
                    and obj.type != LITERAL
                }
                final_pure_geo_objects = {
                    obj
                    for obj in curr_checker.geometry_tracker.all_objects()
                    if not isinstance(obj, ConstructionObject)
                    and not isinstance(obj, EquationObject)
                    and obj.type != LITERAL
                }
                success &= final_pure_geo_objects == pure_geo_objects
                success &= all(
                    curr_checker.geometry_tracker.contains_predicate(pred) for pred in proof.target_predicates
                ) | curr_checker.geometry_tracker.contains_predicate(predicate_from_args('false', ()))
            except ProofCheckError:
                success = False

            if not success:
                # There is a necessary step between curr_i and i.
                low_i = curr_i
                curr_i = (i + curr_i) // 2
                failed_once = True
            else:
                i = curr_i
                curr_i = (curr_i + low_i) // 2

            if not failed_once:
                # If we succeeded the first time, we are done.
                break
            elif i == low_i + 1:
                # Otherwise, we break when we find that we can skip all steps in steps[low:i]
                break

        if failed_once:
            good_steps += 1
            skip_steps[low_i] = False

        i = low_i

    used_steps = [step for step, can_skip_step in zip(proof.steps, skip_steps) if not can_skip_step]

    # Removing unnecessary assumptions.

    if verbose:
        print(f'Skipping assumptions... (t={time.time() - t0:.1f})')
    skip_assumptions = [True] * len(proof.assumption_predicates)

    for i in reversed(range(len(proof.assumption_predicates))):
        curr_checker = checker_before_assumption[i]
        try:
            for assumption, can_skip_assumption in zip(proof.assumption_predicates[i + 1 :], skip_assumptions[i + 1 :]):
                if not can_skip_assumption:
                    curr_checker.geometry_tracker.add_predicate(assumption, ADD_CFG, 'Assumption')

            for step in used_steps:
                curr_checker.add_step(step)
            skip_assumptions[i] &= all(
                curr_checker.geometry_tracker.contains_predicate(pred) for pred in proof.target_predicates
            ) | curr_checker.geometry_tracker.contains_predicate(predicate_from_args('false', ()))
        except ProofCheckError:
            skip_assumptions[i] = False

    used_assumptions = [
        assumption
        for assumption, can_skip_assumption in zip(proof.assumption_predicates, skip_assumptions)
        if not can_skip_assumption
    ]

    if verbose:
        print(f'Skipping objects... (t={time.time() - t0:.1f})')

    skip_objects = [True] * len(proof_objects)
    # Removing unnecessary objects from the proof definition.
    for i in reversed(range(len(proof_objects))):
        curr_checker = checker_before_object[i]
        if any(proof_objects[i] in involved_objects(pred) for pred in used_assumptions):
            skip_objects[i] = False
            continue

        try:
            for obj, can_skip_obj in zip(proof_objects[i + 1 :], skip_objects[i + 1 :]):
                if not can_skip_obj:
                    curr_checker.geometry_tracker.get_object(obj, ADD_CFG)

            for assumption in used_assumptions:
                curr_checker.geometry_tracker.add_predicate(assumption, ADD_CFG, 'Assumption')

            for step in used_steps:
                curr_checker.add_step(step)

            skip_objects[i] &= all(
                curr_checker.geometry_tracker.contains_predicate(pred) for pred in proof.target_predicates
            ) | curr_checker.geometry_tracker.contains_predicate(predicate_from_args('false', ()))
        except ProofCheckError:
            skip_objects[i] = False

    used_objects = {obj.name: obj for obj, can_skip_object in zip(proof_objects, skip_objects) if not can_skip_object}

    # TODO: Remove this once the code has been verified better.

    if false_found:
        target_objects = {}
        target_predicates = [predicate_from_args('false', ())]
    else:
        target_objects = dict(proof.target_objects)
        target_predicates = list(proof.target_predicates)

    res_proof = Proof(
        dict(proof.all_objects),
        used_objects,
        used_assumptions,
        target_objects,
        target_predicates,
        {obj: emb for obj, emb in proof.embeds.items() if obj.name in used_objects},
        used_steps,
    )

    print(res_proof.to_language_format())

    return Proof.parse(res_proof.to_language_format())


def annotate_proof(proof: Proof) -> Proof:
    """
    Adds comments to the theorem steps in the proof, detailing which assumptions are necessary for each theorem step.
    Since fully doing this is complex, I currently use only `compute_requirements_graph_2`.
    """
    proof = proof.shallow_copy()
    assumption_reqs, step_reqs = compute_requirement_graph_2(proof)

    for idx, step in enumerate(proof.steps):
        if not isinstance(step, TheoremStep):
            continue
        reqs = [f'A{i}' for i in assumption_reqs[idx]] + [f'{i}' for i in step_reqs[idx]]
        step.comment = f'({", ".join(reqs)}) -> ({idx})'

    return proof


def max_depth_trim(proof: Proof, target_count: int = 1, verb=False) -> list[Proof]:
    """
    Picks a conclusion for the proof.
    Attempts to get the least trivial subproof.
    When a predicate is added several times, the method here will undercount the steps proving it.

    Parameters:
    * `proof`: The proof that should be trimmed.
    * `target_count`: The number of proofs to attempt to extract from the given proof.
                      When the target count is 0, only a correct proof is extracted from the given proof,
                      and otherwise the whole thing is dropped.
    * `verb`: Whether to print debug data.

    Return:
    A list of proofs not containing any shared statements.
    """
    # If the proof has no theorem steps, then we don't trim it.
    if not any(isinstance(step, TheoremStep) for step in proof.steps):
        return [proof]

    if verb:
        print('Verifying the proof.')
    no_conclusion_proof = proof.shallow_copy()
    no_conclusion_proof.target_predicates = []
    checker = ProofChecker(no_conclusion_proof)
    checker.check()

    if verb:
        print('Checking if the target predicates were proved.')

    # If we have found a contradiction, that is the most improtant thing, since everything after that doesn't realy matter.
    if any(pred.name == 'false' for pred in checker.geometry_tracker._predicates):
        # When `false()` is proved, we just take the proof that the theorem is false.
        proof_successful = True
        proof.target_predicates = [predicate_from_args('false', ())]
        res_proof = trim_proof(proof, verbose=True)
    elif all(checker.geometry_tracker.contains_predicate(pred) for pred in proof.target_predicates):
        proof_successful = True
        res_proof = trim_proof(proof, verbose=True)
    else:
        if target_count == 0:
            return []
        proof.target_predicates = []
        proof_successful = False
        if verb:
            print('Computing initial step requirements.')
        reqs = compute_step_requirements_graph(proof, verb=verb)
        if verb:
            print('Finished computing the step requirements.')
        depth = [0] * len(proof.steps)
        for idx, step in enumerate(proof.steps):
            for req in reqs[idx]:
                depth[idx] = max(depth[idx], depth[req] + 1)
        # Generating the trimmed proof.
        # The last predicate must not be trivial.
        max_idx = max(
            (
                idx
                for idx, step in enumerate(proof.steps)
                if isinstance(step, TheoremStep) and not all(is_trivial(conc) for conc in step.result_predicates)
            ),
            key=lambda i: depth[i],
        )
        max_step = proof.steps[max_idx]
        assert isinstance(max_step, TheoremStep)

        res_proof = proof.shallow_copy()
        res_proof.target_objects = {obj.name: obj for obj in max_step.result_objects}
        for pred in max_step.result_predicates:
            for comp in pred.components:
                for sub_comp in involved_objects(comp):
                    if (
                        not isinstance(sub_comp, ConstructionObject)
                        and not isinstance(sub_comp, EquationObject)
                        and sub_comp.name not in proof.assumption_objects
                        and sub_comp.type != LITERAL
                    ):
                        res_proof.target_objects[sub_comp.name] = sub_comp

        res_proof.target_predicates = max_step.result_predicates
        if verb:
            print('Found the target predicates. Trimming the proof.')
        res_proof = trim_proof(res_proof, verbose=verb)

    reqs = compute_step_requirements_graph(res_proof, verb=verb)
    assumption_reqs = compute_assumption_requirement_graph(res_proof, reqs, verb=verb)

    proof_lst = []

    for idx, (step, as_reqs, step_reqs) in enumerate(zip(res_proof.steps, assumption_reqs, reqs)):
        if isinstance(step, TheoremStep):
            merged_reqs = ', '.join([f"A{i}" for i in sorted(as_reqs)] + [str(i) for i in sorted(step_reqs)])
            step.comment = f'({merged_reqs}) -> ({idx})'

    proof_lst.append(res_proof)

    # Generating the rest of the proofs.
    if target_count > 1 and not proof_successful:
        remaining_proof = proof.shallow_copy()
        remaining_proof.steps = []

        checker = ProofChecker(proof)
        checker.geometry_tracker.load_embeds(proof)
        for obj in proof.assumption_objects.values():
            checker.geometry_tracker.get_object(obj, ADD_CFG)
        for pred in proof.assumption_predicates:
            checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Assumption')
        for pred in proof.auxiliary_predicates:
            checker.geometry_tracker.add_predicate(pred, ADD_CFG, 'Auxiliary')

        removed_idx = 0
        for step in proof.steps:
            if removed_idx < len(res_proof.steps) and step == res_proof.steps[removed_idx]:
                removed_idx += 1
            else:
                try:
                    checker.add_step(step)
                    remaining_proof.steps.append(step)
                except ProofCheckError:
                    ...

        proof_lst.extend(max_depth_trim(remaining_proof, target_count=target_count - 1, verb=verb))

    return proof_lst


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Trims proofs to be as short as possible.')
    parser.add_argument('path', help='The path of the proof file to trim.', type=Path)
    parser.add_argument('-v', help='Prints debug information', action='store_true')
    parser.add_argument(
        '--overwrite',
        help='Overwrite the file with the trimmed proof when trimming is complete.',
        action='store_true',
    )

    args = parser.parse_args()
    path = Proof.get_full_proof_path(args.path)
    proof = Proof.parse(path.open().read())

    t0 = time.time()
    trimmed_proof = trim_proof(proof, verbose=args.v)

    proof_text = trimmed_proof.to_language_format()

    if args.overwrite:
        open(path, 'w').write(proof_text)
    else:
        print(proof_text)

    print(f'Trimmed in {round(time.time() - t0, 2)} seconds')
