from typing import Hashable
from networkx import DiGraph, lowest_common_ancestor
import matplotlib.pyplot as plt
import networkx as nx

from ...union_find.union_find import UnionFind
from ...union_find.labelled_union_find import LabelledUnionFind

from .equations.equation import Equation
from .equations.equation_pair import EquationPair


EDGE_LABEL = 'label'


class ProofForest[T: Hashable]:
    union_find: UnionFind[T]
    forest: DiGraph
    
    def __init__(self):
        self.union_find = UnionFind()
        self.forest = DiGraph()

    def add(self, v_src: T, v_dst: T, e: Equation[T, T] | EquationPair[T]):
        if len(self.union_find.get_equivalences(v_src)) > len(self.union_find.get_equivalences(v_dst)):
            v_src, v_dst = v_dst, v_src

        path_to_root = [v_dst]
        if path_to_root[-1] in self.forest.nodes:
            while True:
                parents = [edge[0] for edge in self.forest.in_edges(path_to_root[-1])]
                if len(parents) == 0:
                    break
                assert len(parents) == 1
                path_to_root.append(parents[0])
        for (dst, src) in zip(path_to_root, path_to_root[1:]):
            attrs = self.forest[src][dst]
            self.forest.remove_edge(src, dst)
            self.forest.add_edge(dst, src, **attrs)
        
        self.forest.add_edge(v_src, v_dst, **{EDGE_LABEL: e})
        self.union_find[v_src] = v_dst

    def get_edge(self, v0: T, v1: T) -> Equation[T, T] | EquationPair[T] | None:
        return self.forest.get_edge_data(v0, v1)[EDGE_LABEL]

    def explain(self, c1: T, c2: T) -> list[Equation[T, T] | EquationPair[T]]:
        additional_union_find = LabelledUnionFind(lambda t: t, lambda t1, l1, t2, l2: l2)
        pending_proofs = [(c1, c2)]
        proof: list[Equation[T, T] | EquationPair[T]] = []
        
        while len(pending_proofs) > 0:
            (a, b) = pending_proofs.pop()
            if a == b:
                continue
            c = lowest_common_ancestor(self.forest, a, b)
            proof.extend(self.explain_along_path(additional_union_find, pending_proofs, a, c))
            proof.extend(self.explain_along_path(additional_union_find, pending_proofs, b, c))
        return proof
    
    def explain_along_path(self, additional_union_find: LabelledUnionFind[T, T], pending_proofs: list[tuple[T, T]], a: T, c: T) -> list[Equation[T, T] | EquationPair[T]]:
        a = additional_union_find.get_label(a)
        c = additional_union_find.get_label(c)
        proof: list[Equation[T, T] | EquationPair[T]] = []
        while a != c:
            b = list(self.forest.predecessors(a))[0]
            edge = self.get_edge(b, a)
            if isinstance(edge, Equation):
                proof.append(edge)
            elif isinstance(edge, EquationPair):
                proof.append(edge)
                for (a_parameter, b_parameter) in zip(edge.left_term.parameters, edge.right_term.parameters):
                    pending_proofs.append((a_parameter, b_parameter))
            additional_union_find[a] = b
            a = additional_union_find.get_label(b)
        return proof

    def debug_draw(self):
        pos = nx.spring_layout(self.forest, k=5)
        edge_labels = dict([((n1, n2), str(self.forest[n1][n2][EDGE_LABEL])) for n1, n2 in self.forest.edges])
        nx.draw_networkx(self.forest, pos)
        nx.draw_networkx_edge_labels(self.forest, pos, edge_labels=edge_labels)
        plt.show()
