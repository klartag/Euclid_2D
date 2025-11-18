from typing import Generic, Hashable, TypeVar, cast
from networkx import DiGraph

from ...union_find import UnionFind

from .equations.equation import Equation
from .equations.equation_pair import EquationPair


EDGE_LABEL = 'label'


class ProofForest[T: Hashable]:
    forest: DiGraph
    
    def __init__(self):
        self.forest = DiGraph()
        
    def add(self, v0: T, v1: T, e: Equation[T, T] | EquationPair[T]):
        self.forest.add_edge(v0, v1, attr={EDGE_LABEL: e})
        
    def get_edge(self, v0: T, v1: T) -> Equation[T, T] | EquationPair[T] | None:
        return self.forest.get_edge_data(v0, v1)[EDGE_LABEL]

    def explain(self, c1: T, c2: T) -> list[Equation[T, T] | EquationPair[T]]:
        union_find = UnionFind[T]()
        pending_proofs = [(c1, c2)]
        proof: list[Equation[T, T] | EquationPair[T]] = []
        
        while len(pending_proofs) > 0:
            (a, b) = pending_proofs.pop()
            c = self.nearest_common_ancestor(a, b)
            proof.extend(self.explain_along_path(union_find, pending_proofs, a, c))
            proof.extend(self.explain_along_path(union_find, pending_proofs, b, c))
        return proof
    
    def explain_along_path(self, union_find: UnionFind[T], pending_proofs: list[tuple[T, T]], a: T, c: T) -> list[Equation[T, T] | EquationPair[T]]:
        a = self.get_highest_node(a)
        proof: list[Equation[T, T] | EquationPair[T]] = []
        while a != c:
            b = self.parent(a)
            edge = self.get_edge(a, b)
            if isinstance(edge, Equation):
                proof.append(edge)
            elif isinstance(edge, EquationPair):
                proof.append(edge)
                for (a_parameter, b_parameter) in zip(edge.left_term.parameters, edge.right_term.parameters):
                    pending_proofs.append((a_parameter, b_parameter))
            union_find[a] = b
            a = self.get_highest_node(b)
        return proof
    
    def nearest_common_ancestor(self, v0: T, v1: T) -> T:
        raise NotImplementedError()
    
    def get_highest_node(self, v: T) -> T:
        raise NotImplementedError()
    
    def set_highest_node(self, v0: T, v1: T):
        raise NotImplementedError()
    
    def parent(self, v: T) -> T:
        raise NotImplementedError()