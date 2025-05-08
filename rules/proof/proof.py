from collections import defaultdict
import itertools
import json
import random
import string
from typing import Optional

from util import BASE_PATH

from ..rule_utils import LITERAL
from ..embeddings import Embedding
from ..predicates.predicate import Predicate
from ..geometry_objects.construction_object import ConstructionObject
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject

from .steps import ObjDefineStep, Step, TheoremStep

ASSUMPTION_TITLE = 'Assumptions:'
TARGET_TITLE = 'Need to prove:'
EMBED_TITLE = 'Embedding:'
BODY_TITLE = 'Proof:'

LINE_BREAK = '\n'


class Proof:
    """
    A class representing a proof.
    Stores a list of involved objects and the theorems applied on them,
    while doing no verification.
    The format in which a proof is stored is detailed in the language specification document.
    """

    all_objects: dict[str, GeoObject]
    assumption_objects: dict[str, GeoObject]
    assumption_predicates: list[Predicate]
    auxiliary_predicates: list[Predicate]
    target_objects: dict[str, GeoObject]
    target_predicates: list[Predicate]
    embedding: Optional[Embedding]
    steps: list[Step]

    def __init__(
        self,
        objects: dict[str, GeoObject],
        assumption_objects: dict[str, GeoObject],
        assumption_predicates: list[Predicate],
        auxiliary_predicates: list[Predicate],
        target_objects: dict[str, GeoObject],
        target_predicates: list[Predicate],
        embedding: Optional[Embedding],
        steps: list[Step],
    ):
        self.all_objects = objects
        self.assumption_objects = assumption_objects
        self.assumption_predicates = assumption_predicates
        self.auxiliary_predicates = auxiliary_predicates
        self.target_objects = target_objects
        self.target_predicates = target_predicates
        self.embedding = embedding
        self.steps = steps

    def to_language_format(self) -> str:
        """
        Converts the proof to a human readable format.
        @return: A string containing the proof.
        """
        assumptions = [ASSUMPTION_TITLE]
        embeds = [EMBED_TITLE]
        need_to_prove = [TARGET_TITLE]
        proof_body = [BODY_TITLE]

        # Representing the assumptions.
        objects_by_type = defaultdict(list)
        for obj in self.assumption_objects.values():
            if obj not in self.target_objects:
                objects_by_type[obj.type].append(obj)

        for type_, objects in objects_by_type.items():
            assumptions.append(', '.join(obj.name for obj in objects) + ': ' + type_)

        for known_pred in self.assumption_predicates:
            assumptions.append(known_pred.to_language_format())

        # Representing the embeds.
        if self.embedding is not None:
            for name, embedded_object in self.embedding.items():
                embeds.append(f'{name} := {json.dumps(embedded_object.to_dict())}')
        else:
            embeds = []

        # Representing the need-to-prove.
        objects_by_type = defaultdict(list)
        for obj in self.target_objects.values():
            objects_by_type[obj.type].append(obj)

        for type_, objects in objects_by_type.items():
            need_to_prove.append(', '.join(obj.name for obj in objects) + ': ' + type_)

        for pred in self.target_predicates:
            need_to_prove.append(pred.to_language_format())

        # Representing the steps.
        for step in self.steps:
            proof_body.append(step.to_language_format())

        assumptions_string = '\n'.join(assumptions)
        embeds_string = '\n'.join(embeds)
        need_to_prove_string = '\n'.join(need_to_prove)
        proof_body_string = '\n'.join(proof_body)

        proof_string = '\n\n'.join(
            filter(None, [assumptions_string, embeds_string, need_to_prove_string, proof_body_string])
        )

        return proof_string + '\n'

    def shuffled(self):
        """
        Shuffles the names of the objects in the proof.
        """
        out_names = set()

        def gen_name(obj: GeoObject) -> str:
            """
            Generates a name for an object.
            """
            type_prefix = obj.type[0].lower() + '_'
            l = 1
            attempts = 0
            while (
                new_name := type_prefix + ''.join(random.choice(string.ascii_uppercase) for _ in range(l))
            ) in out_names:
                attempts += 1
                if attempts == 5:
                    l += 1
                    attempts = 0

            out_names.add(new_name)
            return new_name

        # Due to possible conclusions, this is no longer allowed.
        # random.shuffle(self.assumptions)

        subs = {}
        for obj in itertools.chain(
            self.assumption_objects.values(),
            self.target_objects.values(),
            sum((step.result_objects for step in self.steps if isinstance(step, TheoremStep)), []),
            (step.left_hand for step in self.steps if isinstance(step, ObjDefineStep)),
        ):
            if (not isinstance(obj, ConstructionObject) or isinstance(obj, EquationObject)) and obj.type != LITERAL:
                new_obj = GeoObject(gen_name(obj), obj.type)
                subs[obj] = new_obj

        res_assumption_objects = {}
        res_target_objects = {}
        res_assumption_predicates = []
        res_auxiliary_predicates = []
        res_targets = []
        res_steps = []

        for obj in self.assumption_objects.values():
            res_obj = obj.substitute(subs)
            res_assumption_objects[res_obj.name] = res_obj

        for obj in self.target_objects.values():
            res_obj = obj.substitute(subs)
            res_target_objects[res_obj.name] = res_obj

        for assumption in self.assumption_predicates:
            res_assumption_predicates.append(assumption.substitute(subs))

        for auxiliary_predicate in self.auxiliary_predicates:
            res_auxiliary_predicates.append(auxiliary_predicate.substitute(subs))

        for target_predicate in self.target_predicates:
            res_targets.append(target_predicate.substitute(subs))

        for step in self.steps:
            res_steps.append(step.substitute(subs))

        res_embeds = None
        if self.embedding is not None:
            res_embeds = {}
            for name, embedded_object in self.embedding.items():
                new_name = [value for obj, value in subs.items() if obj.name == name][0]
                res_embeds[new_name] = embedded_object

        return Proof(
            res_assumption_objects | res_target_objects,
            res_assumption_objects,
            res_assumption_predicates,
            res_auxiliary_predicates,
            res_target_objects,
            res_targets,
            res_embeds,
            res_steps,
        )

    def shallow_copy(self) -> 'Proof':
        """
        Returns a shallow copy of the proof.
        This makes duplicates of the proof's structures,
        but copies the references to all underlying objects.
        """
        return Proof(
            dict(self.all_objects),
            dict(self.assumption_objects),
            list(self.assumption_predicates),
            list(self.auxiliary_predicates),
            dict(self.target_objects),
            list(self.target_predicates),
            self.embedding.shallow_copy() if self.embedding is not None else None,
            list(self.steps),
        )

    def strip_comments(self) -> 'Proof':
        """
        Removes all comments from the proof.
        """
        res = self.shallow_copy()
        for step in res.steps:
            if isinstance(step, TheoremStep):
                step.comment = ''
        return res

    def starting_predicates(self) -> list[Predicate]:
        return self.assumption_predicates + self.auxiliary_predicates


def test_pretty_print():
    path = BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G2.txt'
    proof = Proof.parse(path.open().read())
    print(proof.to_language_format())


def test_shuffle():
    proof = Proof.parse((BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G3.jl').open().read())

    print(proof.shuffled().to_language_format())


def test_parse():
    proof = Proof.parse((BASE_PATH / 'rules/proof_samples/IMO_2022_shortlist_G2_numeric.jl').open().read())
    print(proof.to_language_format())


if __name__ == '__main__':
    # test_pretty_print()
    # test_shuffle()
    test_parse()
