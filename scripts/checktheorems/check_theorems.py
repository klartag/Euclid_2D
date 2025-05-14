import sys
import os

from rules.rule_utils import CIRCLE, POINT

sys.path.append(os.path.dirname(__file__) + "/../..")


from rules.geometry_configuration.geo_config import GeoConfig
from rules.predicates.predicate import PREDICATE_SIGNATURES

from rules.theorem import Theorem, THEOREM_FOLDER
from pathlib import Path
from tqdm import tqdm
import random
from matplotlib import pyplot as plt
import torch
import numpy as np
import glob
import random
from rules.geometry_objects.construction_object import *
from rules.geometry_objects.geo_object import GeoObject
from rules.pred_config import *
from rules.predicates.predicate_factory import parse_predicate, predicate_from_args

load_constructions_and_macros()

from tqdm import tqdm
import string
from ordered_set import OrderedSet
import math
import copy
import json


def sample_predicates(
    type_obj,
    candidate_predicates=[
        "between",
        "equals",
        "equals_mod_180",
        "equals_mod_360",
        "in",
        "between",
        "tangent",
        "parallel",
        "perpendicular",
        "collinear",
        "concyclic",
        "concurrent",
    ],
    num_samples=3,
):
    if candidate_predicates is None:
        candidate_predicates = list(PREDICATE_SIGNATURES.keys())
        candidate_predicates.remove("false")
        candidate_predicates.remove("inside_triangle")
        candidate_predicates.remove("outside_triangle")
    sampled_predicates = []
    for idx in range(num_samples):
        pred_name = random.choice(candidate_predicates)
        object_types = random.choice(PREDICATE_SIGNATURES[pred_name])
        can_find_type_match = True
        for type in OrderedSet(object_types):
            count = object_types.count(type)
            if type not in type_obj or count > len(type_obj[type]):
                can_find_type_match = False
        if can_find_type_match:
            args = []
            for type in OrderedSet(object_types):
                args += random.sample(list(type_obj[type]), object_types.count(type))
            sampled_predicates.append(Predicate.from_args(pred_name, tuple(args)))
    return sampled_predicates


def check_compatibility(
    construction,
    type_obj_map,
    score_assignments={"Point": 1, "Line": 2, "Triangle": 5, "Circle": 10, "Scalar": 1, "Angle": 1, "Orientation": 1},
):
    target_map = construction.get_type_object_map()
    score = 0
    for type, objects in target_map.items():
        if type in type_obj_map and len(objects) <= len(type_obj_map[type]):
            score += score_assignments[type]
        else:
            return 0
    return score


def couple_objects(const_or_theorem, obj_map, type_obj_map, p=0.8):
    if isinstance(const_or_theorem, Construction):
        p = 1
    target_map = const_or_theorem.get_type_object_map()
    replacements = {}
    for type, objects in target_map.items():
        num_objects_to_couple = math.ceil(len(target_map[type]) * p)
        if type in type_obj_map:
            sampled_objects = random.sample(type_obj_map[type], num_objects_to_couple)
            replacements.update(dict(zip(objects, sampled_objects)))

    if isinstance(const_or_theorem, Construction):
        return const_or_theorem().substitute(replacements)
    elif isinstance(const_or_theorem, Theorem):
        existing_names = OrderedSet(obj_map.keys())
        for _, obj in const_or_theorem_obj_map.items():
            new_objects = []
            if not isinstance(obj, ConstructionObject) and obj not in replacements:
                # new_objects.append(obj)
                new_name = get_new_name(obj, existing_names)
                new_object = obj.replicate_with_name(new_name)
                replacements.update({obj: new_object})
                new_objects.append(new_object)

        new_predicates = [pred.substitute(replacements) for pred in const_or_theorem.required_predicates]
        return new_predicates, new_objects


def get_new_name(object, existing_names):
    match object.type:
        case "Point":
            names = string.ascii_uppercase
        case "Line":
            names = [f"l{idx}" for idx in range(1, 27)]
        case "Circle":
            names = [f"c{idx}" for idx in range(1, 27)]
        case "Triangle":
            names = [f"t{idx}" for idx in range(1, 27)]
        case "Scalar" | "Angle" | "Orientation":
            names = string.ascii_lowercase
        case _:
            print(object.type)
            raise NotImplementedError()
    candidate_names = OrderedSet(names) - OrderedSet(existing_names)
    if len(candidate_names) == 0:
        raise NotImplementedError("need more names!")

    name = candidate_names.pop(0)
    return name


def add_object(object, obj_map, type_obj_map):
    obj_map[object.name] = object
    # print("in add_object", object)
    if object.type not in type_obj_map:
        type_obj_map[object.type] = [object]
    else:
        type_obj_map[object.type].append(object)

    return obj_map, type_obj_map


def rename_theorem_objects(theorem):
    for _, object in theorem_obj_map.items():
        object.update_name("new_" + object.name)


def construct_new_object(all_constructions, obj_map, type_obj_map):
    scores = []
    for construction in all_constructions:
        score = check_compatibility(construction, type_obj_map)
        scores.append(score)
    # print(obj_map, type_obj_map, scores)
    construction = random.choices(all_constructions, weights=scores, k=1)[0]
    new_object = couple_objects(construction, obj_map, type_obj_map)
    # print(new_object, type_obj_map)
    existing_names = OrderedSet(obj_map.keys())
    new_name = get_new_name(new_object, existing_names)
    new_object.update_name(new_name)
    obj_map, type_obj_map = add_object(new_object, obj_map, type_obj_map)
    # print(type_obj_map)
    return new_object, obj_map, type_obj_map


def add_new_theorem(all_theorems, obj_map, type_obj_map):
    scores = []
    for theorem in all_theorems:
        score = check_compatibility(theorem, type_obj_map)
        scores.append(score)

    sampled_theorem = copy.deepcopy(random.choices(all_theorems, weights=scores, k=1)[0])
    rename_theorem_objects(sampled_theorem)
    new_predicates, new_objects = couple_objects(sampled_theorem, obj_map, type_obj_map)
    for object in new_objects:
        obj_map, type_obj_map = add_object(object, obj_map, type_obj_map)

    return new_predicates, obj_map, type_obj_map


def check_theorem(theorem, idx, seed=100):
    local_rank = idx % torch.cuda.device_count()
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed * 2)
    np.random.seed(seed * 3)
    random.seed(seed * 4)
    theorem = copy.deepcopy(theorem)
    predicates = []

    result_str = None

    # existing_names = OrderedSet(theorem_obj_map.keys())
    existing_names = OrderedSet([obj.name for obj in theorem.signature])
    theorem_obj_map = {obj.name: obj for obj in theorem.signature}
    for pred in theorem.required_predicates:
        if pred.name == "exists":
            continue
        elif pred.name == "tangent" and pred.components[0].type == "Circle" and pred.components[1].type == "Circle":
            predicates.append(pred)
            predicates.append(
                parse_predicate(f"distinct({pred.components[0].name}, {pred.components[1].name})", theorem_obj_map)
            )
        elif pred.name == "concyclic":
            new_circle = Atom("new_circle", CIRCLE)
            new_name = get_new_name(new_circle, existing_names)
            existing_names.add(new_name)
            new_circle.name = new_name
            theorem_obj_map.update({new_name: new_circle})
            for point in pred.components:
                predicates.append(parse_predicate(f"{point.name} in {new_name}", theorem_obj_map))
            distinct_pred_str = "distinct(" + ",".join([point.name for point in pred.components]) + ")"
            predicates.append(parse_predicate(distinct_pred_str, theorem_obj_map))
        elif pred.name == "concurrent":
            new_point = Atom("new_point", POINT)
            new_name = get_new_name(new_point, existing_names)
            existing_names.add(new_name)
            new_point.update_name(new_name)
            theorem_obj_map.update({new_name: new_point})
            for line in pred.components:
                predicates.append(parse_predicate(f"{new_name} in {line.name}", theorem_obj_map))
            distinct_pred_str = "distinct(" + ",".join([line.name for line in pred.components]) + ")"
            predicates.append(parse_predicate(distinct_pred_str, theorem_obj_map))
        elif pred.name == "inside_triangle":
            O, A, B, C = pred.components
            predicates.append(parse_predicate(f"triangle({A},{B},{C})", theorem_obj_map))
            predicates.append(
                parse_predicate(
                    f"identical(orientation({A}, {B}, {O}), orientation({B}, {C}, {O}), orientation({C}, {A}, {O}))",
                    theorem_obj_map,
                )
            )
        else:
            predicates.append(pred)

    for name, object in theorem_obj_map.items():
        if object.type == "Circle":
            predicates.append(parse_predicate(f"radius({object.name}) != 0", theorem_obj_map))

    obj_map = theorem_obj_map
    type_obj_map = theorem.get_type_object_map()

    result_predicates = theorem.result_predicates

    config = GeoConfig(obj_map, predicates)

    init_params = torch.randn(10000, config.num_params, requires_grad=True, device=local_rank)

    if len(predicates) > 0:
        params = torch.randn(1, config.num_params, requires_grad=True, device=local_rank)
        hessian = config.hessian(params[0])
        eigvals = torch.linalg.eigvalsh(hessian)
        max_eigval = eigvals.max().item()
        if max_eigval > 0:
            lr = 1 / max_eigval
        else:
            lr = 2

        losses, params = config.batch_sgd(init_params, max_iter=2000, lr=lr, momentum=0.5, weight_decay=1e-3)
        losses, params = config.batch_sgd(params, max_iter=2000, lr=lr / 10, momentum=0.5, weight_decay=1e-3)
        losses, params = config.batch_sgd(params, max_iter=1000, lr=lr / 20, momentum=0, weight_decay=0)
    else:
        result_str = str(idx) + f", no predicates, {theorem}, {theorem.path.relative_to(THEOREM_FOLDER)}" + "\n"
        return True, result_str

    good_idx = ~torch.isnan(losses)
    good_params = params[good_idx]
    good_losses = losses[good_idx]
    if good_losses.numel() > 0:
        if good_losses.min().item() > 1e-4:
            result_str = str(idx) + f", train loss, {theorem}, {theorem.path.relative_to(THEOREM_FOLDER)}" + "\n"
            return False, result_str

        best_params = good_params[good_losses.argmin()]

        result_predicates = predicates if "construct" in theorem.data else result_predicates
        final_result_predicates = []
        for pred in result_predicates:
            if pred.name == "exists":
                continue
            elif pred.name == "inside_triangle":
                O, A, B, C = pred.components
                final_result_predicates.append(parse_predicate(f"triangle({A},{B},{C})", theorem_obj_map))
                final_result_predicates.append(
                    parse_predicate(
                        f"identical(orientation({A}, {B}, {O}), orientation({B}, {C}, {O}), orientation({C}, {A}, {O}))",
                        theorem_obj_map,
                    )
                )
            else:
                final_result_predicates.append(pred)
        results = config.verify_predicates(final_result_predicates, best_params)
        for pred, loss in results.items():
            if loss > 5e-3:
                result_str = str(idx) + f", result loss, {theorem}, {theorem.path.relative_to(THEOREM_FOLDER)}" + "\n"
                break

    if result_str is None:
        correct = True
        result_str = str(idx) + f", success, {theorem}, {theorem.path.relative_to(THEOREM_FOLDER)}" + "\n"
    else:
        correct = False

    return correct, result_str


def worker(theorem, idx, seed):
    if "contradictions/" in theorem.path.as_posix():
        return
    try:
        correct, result_str = check_theorem(theorem, idx, seed)
    except Exception as err:
        correct = False
        result_str = str(idx) + f", bug, {theorem}, {theorem.path.relative_to(THEOREM_FOLDER)}\n{err}" + "\n"
    with lock:
        with open(output_file, "a") as fp:
            fp.write(json.dumps({"idx": idx, "correct": correct, "result_str": result_str}) + "\n")


from pebble import ProcessPool
from multiprocessing import Lock

seed = 100

output_file = "check_theorems_results.jsonl"

all_constructions = global_predicates.get_constructions()

all_theorems = list(Theorem.all_theorems().values())

lock = Lock()
if __name__ == "__main__":
    if os.path.exists(output_file):
        os.remove(output_file)
    with ProcessPool(max_workers=8) as pool:
        futures = []
        for idx, theorem in enumerate(all_theorems):
            future = pool.schedule(worker, (theorem, idx, seed))
            futures.append(future)

        for future in tqdm(futures):
            future.result()
