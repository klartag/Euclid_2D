if __name__ == '__main__':
    # Dealing with path issues.
    from os.path import dirname, abspath
    import sys

    sys.path.append(dirname(dirname(abspath(__file__))))

from matplotlib import pyplot as plt
from typing import Dict
from adjustText import adjust_text
import random
from tqdm import tqdm

from .evaluate_geo_object import *
from .torch_geo.geometry_entities import *

from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.construction_object import ConstructionObject


def fully_unpack_predicate(predicate):

    if predicate.name in ["triangle", "between", "inside_triangle"]:
        unpacked = [predicate]
    else:
        unpacked = predicate.unpack()

    if unpacked[0] == predicate:
        return [predicate]

    results = []
    for pred in unpacked:
        results.extend(fully_unpack_predicate(pred))

    return results


class GeoConfig:
    def __init__(self, obj_map: Dict[str, GeoObject], predicates):
        self.obj_map = obj_map
        self.predicates = []
        for pred in predicates:
            self.predicates.extend(fully_unpack_predicate(pred))

        self.num_params = 0
        for name, geo_object in self.obj_map.items():
            if isinstance(geo_object, ConstructionObject):
                continue
            name = geo_object.name
            type = geo_object.type
            match type:
                case "Scalar" | "Angle" | "Orientation":
                    self.num_params += 1
                case "Point":
                    self.num_params += 2
                case "Line":
                    self.num_params += 4
                case "Triangle":
                    self.num_params += 6
                case "Circle":
                    self.num_params += 3
                case "Scalar":
                    self.num_params += 1

    def get_torch_objects(self, params):
        torch_obj_map = {}
        idx = 0
        for name, geo_object in self.obj_map.items():
            if isinstance(geo_object, ConstructionObject):
                continue
            name = geo_object.name
            type = geo_object.type
            match type:
                case "Literal":
                    torch_object = torch.tensor(float(name), requires_grad=False).to(params.device)
                case "Scalar" | "Angle" | "Orientation":
                    torch_object = params[idx]
                    idx += 1
                case "Point":
                    torch_object = Point(params[idx], params[idx + 1])
                    idx += 2
                case "Line":
                    torch_object = Line(Point(params[idx], params[idx + 1]), Point(params[idx + 2], params[idx + 3]))
                    idx += 4
                case "Triangle":
                    torch_object = Triangle(
                        Point(params[idx], params[idx + 1]),
                        Point(params[idx + 2], params[idx + 3]),
                        Point(params[idx + 4], params[idx + 5]),
                    )
                    idx += 6
                case "Circle":
                    torch_object = Circle(Point(params[idx], params[idx + 1]), torch.abs(params[idx + 2]))
                    idx += 3
                case "Scalar":
                    torch_object = params[idx]
                    idx += 1
            torch_obj_map[name] = torch_object

        for name, geo_object in self.obj_map.items():
            if isinstance(geo_object, ConstructionObject):
                torch_obj_map[name] = evaluate_construction(geo_object, torch_obj_map)

        return torch_obj_map

    def compute_loss(self, params):
        torch_obj_map = self.get_torch_objects(params)
        loss = 0
        for p in self.predicates:
            loss += p.potential(torch_obj_map) / len(self.predicates)
        return loss

    def batch_sgd(self, all_params, max_iter=1000, lr=1, momentum=0.5, weight_decay=1e-4):

        batch_compute_loss = torch.vmap(self.compute_loss)

        optimizer = torch.optim.SGD([all_params], lr=lr, momentum=momentum, weight_decay=weight_decay)
        for it in tqdm(range(max_iter), disable=True):
            optimizer.zero_grad()
            losses = batch_compute_loss(all_params)
            total_loss = losses.sum()
            total_loss.backward()
            optimizer.step()

        losses = batch_compute_loss(all_params)

        return losses, all_params

    def hessian(self, params):
        hessian = torch.autograd.functional.hessian(self.compute_loss, params)
        return hessian

    def newton_step(self, params, num_steps=10, weight_decay=100):

        for it in range(num_steps):
            grad = torch.autograd.functional.jacobian(self.compute_loss, params)
            hessian = torch.autograd.functional.hessian(self.compute_loss, params)
            hessian_inv = torch.linalg.inv(hessian + weight_decay * torch.eye(hessian.size(0), device=hessian.device))
            params.data -= hessian_inv @ grad

        with torch.no_grad():
            loss = func(self.torch_params)
            return loss.item()

    def verify_predicates(self, predicates, params, eps=0):
        with torch.no_grad():
            torch_obj_map = self.get_torch_objects(params)
            all_predicates = []
            for pred in predicates:
                all_predicates.extend(fully_unpack_predicate(pred))

            return {p: p.potential(torch_obj_map, eps=eps).item() for p in all_predicates}

    def plot(self, params, fig=None):
        with torch.no_grad():
            # self.torch_obj_map = self.get_torch_objects(self.obj_map, self.torch_params)
            torch_obj_map = self.get_torch_objects(params)
            # for p in self.predicates:
            #     p.potential(torch_obj_map) / len(self.predicates)
            plt.ioff()
            if not fig:
                fig = plt.figure()

            ax = fig.gca()
            texts = []
            for name, object in torch_obj_map.items():
                if isinstance(object, Point):
                    point = object
                    x, y = point.x.item(), point.y.item()
                    ax.plot(x, y, marker='o')
                    if "(" not in name:
                        texts.append(ax.text(x, y, name))
                    # ax.annotate(name, (x+0.05, y+0.05))
                elif isinstance(object, Line):
                    p1, p2 = object.p1, object.p2
                    ax.plot([p1.x.item(), p2.x.item()], [p1.y.item(), p2.y.item()])
                    if "(" not in name:
                        texts.append(ax.text((p1.x.item() + p2.x.item()) / 2, (p1.y.item() + p2.y.item()) / 2, name))
                elif isinstance(object, Triangle):
                    p1, p2, p3 = object.p1, object.p2, object.p3
                    ax.plot(
                        [p1.x.item(), p2.x.item(), p3.x.item(), p1.x.item()],
                        [p1.y.item(), p2.y.item(), p3.y.item(), p1.y.item()],
                    )
                elif isinstance(object, Circle):
                    center = object.center
                    radius = object.radius.item()
                    Ox, Oy = center.x.item(), center.y.item()
                    patch = plt.Circle((Ox, Oy), radius, fill=False)
                    if "(" not in name:
                        texts.append(ax.text(Ox, Oy, f"O_{name}"))
                        ax.add_patch(patch)

            adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
            ax.set_aspect('equal')
            return fig


def sample_theorem_assumptions(candidate_theorems=None, num_samples=2):
    sampled_theorems = random.choices(candidate_theorems, k=num_samples)
    predicates = []
    for idx, theorem in enumerate(sampled_theorems):
        replacement = {}
        for obj in theorem.signature:
            replacement[obj] = GeoObject(f"t{idx}_" + obj.name, obj.type)

        for pred in theorem.required_predicates:
            pred = pred.substitute(replacement)
            predicates.append(pred)

    return predicates


def sample_predicates(candidate_predicates=None, num_samples=2):
    if candidate_predicates is None:
        candidate_predicates = list(PREDICATE_SIGNATURES.keys())
        candidate_predicates.remove("false")
    sampled_predicates = []
    for idx, pred_name in enumerate(random.choices(candidate_predicates, k=num_samples)):
        success = False
        while not success:
            object_types = random.choice(PREDICATE_SIGNATURES[pred_name])
            success = "Literal" not in object_types
        pred_objects = []
        for obj_idx, obj_type in enumerate(object_types):
            obj_name = f"p{idx}_{obj_idx}"
            pred_objects.append(GeoObject(obj_name, obj_type))
        sampled_predicates.append(Predicate.from_args(pred_name, tuple(pred_objects)))
    return sampled_predicates
