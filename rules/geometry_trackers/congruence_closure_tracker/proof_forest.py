from typing import Hashable, Literal
from networkx import DiGraph, lowest_common_ancestor
import matplotlib.pyplot as plt
import networkx as nx

from ...union_find.union_find import UnionFind
from ...union_find.labelled_union_find import LabelledUnionFind

from .equations.equation import Equation
from .equations.equation_pair import EquationPair


EDGE_ATTRIBUTE = 'edge'


class ProofForest[T: Hashable, L]:
    union_find: UnionFind[T]
    forest: DiGraph
    
    def __init__(self):
        self.union_find = UnionFind()
        self.forest = DiGraph()

    def add(self, v_src: T, v_dst: T, edge: Equation[T, T, L] | EquationPair[T, L]):
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
        
        self.forest.add_edge(v_src, v_dst, **{EDGE_ATTRIBUTE: edge})
        self.union_find[v_src] = v_dst

    def get_edge(self, v0: T, v1: T) -> Equation[T, T, L] | EquationPair[T, L] | None:
        return self.forest.get_edge_data(v0, v1)[EDGE_ATTRIBUTE]

    def explain(self, c1: T, c2: T) -> list[L]:
        additional_union_find = LabelledUnionFind(lambda t: t, lambda t1, l1, t2, l2: l2)
        pending_proofs = [(c1, c2)]
        proof: set[L] = set()
        
        while len(pending_proofs) > 0:
            (a, b) = pending_proofs.pop()
            if a == b:
                continue
            c = lowest_common_ancestor(self.forest, a, b)
            path = self.explain_along_path(additional_union_find, pending_proofs, a, c)
            print(a, c, path)
            proof.update(path)
            path = self.explain_along_path(additional_union_find, pending_proofs, b, c)
            print(b, c, path)
            proof.update(path)
        return list(proof)
    
    def explain_along_path(self, additional_union_find: LabelledUnionFind[T, T], pending_proofs: list[tuple[T, T]], a: T, c: T) -> list[L]:
        a = additional_union_find.get_label(a)
        c = additional_union_find.get_label(c)
        proof: list[L] = []
        while a != c:
            b = list(self.forest.predecessors(a))[0]
            edge = self.get_edge(b, a)
            if edge is not None and edge.predicate is not None:
                proof.append(edge.predicate)
            if isinstance(edge, EquationPair):
                if edge.second_predicate is not None:
                    proof.append(edge.second_predicate)
                for (a_parameter, b_parameter) in zip(edge.left_term.parameters, edge.right_term.parameters):
                    pending_proofs.append((a_parameter, b_parameter))
            additional_union_find[a] = b
            a = additional_union_find.get_label(b)
        return proof

    def debug_draw(self):
        pos = nx.spring_layout(self.forest, k=5)
        edge_labels = dict([((n1, n2), str(self.forest[n1][n2][EDGE_ATTRIBUTE])) for n1, n2 in self.forest.edges])
        nx.draw_networkx(self.forest, pos)
        nx.draw_networkx_edge_labels(self.forest, pos, edge_labels=edge_labels)
        plt.show()
