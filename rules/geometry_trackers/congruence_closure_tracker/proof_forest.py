from typing import Hashable
from networkx import DiGraph, lowest_common_ancestor

from ...union_find import UnionFind

from .equations.equation import Equation
from .equations.equation_pair import EquationPair


EDGE_LABEL = 'label'


class ProofForest[T: Hashable]:
    union_find: UnionFind[T]
    forest: DiGraph
    
    def __init__(self):
        self.union_find = UnionFind()
        self.forest = DiGraph()

    def add(self, v0: T, v1: T, e: Equation[T, T] | EquationPair[T]):
        if len(self.union_find.get_equivalences(v0)) > len(self.union_find.get_equivalences(v1)):
            v0, v1 = v1, v0
        
        path_to_root = [v0]
        if path_to_root[-1] in self.forest.nodes:
            while True:
                parents = [edge[1] for edge in self.forest.out_edges(path_to_root[-1])]
                if len(parents) == 0:
                    break
                assert len(parents) == 1
                path_to_root.append(parents[0])
            for (src, dst) in zip(path_to_root, path_to_root[1:]):
                attrs = self.forest[src][dst]
                self.forest.remove_edge(src, dst)
                self.forest.add_edge(dst, src, **attrs)
        
        self.forest.add_edge(v0, v1, **{EDGE_LABEL: e})
        self.union_find[v0] = v1
        
    def get_edge(self, v0: T, v1: T) -> Equation[T, T] | EquationPair[T] | None:
        return self.forest.get_edge_data(v0, v1)[EDGE_LABEL]

    def explain(self, c1: T, c2: T) -> list[Equation[T, T] | EquationPair[T]]:
        union_find = UnionFind[T]()
        pending_proofs = [(c1, c2)]
        proof: list[Equation[T, T] | EquationPair[T]] = []
        
        while len(pending_proofs) > 0:
            (a, b) = pending_proofs.pop()
            c = lowest_common_ancestor(self.forest, a, b)
            proof.extend(self.explain_along_path(union_find, pending_proofs, a, c))
            proof.extend(self.explain_along_path(union_find, pending_proofs, b, c))
        return proof
    
    def explain_along_path(self, union_find: UnionFind[T], pending_proofs: list[tuple[T, T]], a: T, c: T) -> list[Equation[T, T] | EquationPair[T]]:
        a = self.get_highest_node(a)
        proof: list[Equation[T, T] | EquationPair[T]] = []
        while a != c:
            b = list(self.forest.predecessors(a))[0]
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
    
    def get_highest_node(self, v: T) -> T:
        raise NotImplementedError()
    
    def set_highest_node(self, v0: T, v1: T):
        raise NotImplementedError()
