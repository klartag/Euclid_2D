from collections import defaultdict
import itertools
from pathlib import Path
from typing import Dict, List, Mapping, Optional


from ...embeddings.undefined_embedding_error import UndefinedEmbeddingError
from ...rule_utils import POINT
from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.construction_object import ConstructionObject
from ...predicates.predicate import Predicate
from ...predicates.implementations.distinct_predicate import DistinctPredicate
from ...predicates.predicate_factory import predicate_from_args
from ...proof import Proof

from .. import Embedding
from ..embedded_predicate_value import EmbeddedPredicateValue

from .construction_patterns.implementations import CONSTRUCTION_PATTERNS
from .embedded_constructions.embedded_construction import EmbeddedConstruction


EMBEDDING_ATTEMPTS = 1000


class DiagramEmbedder:
    def try_sequence_object(
        self, object_: GeoObject, predicates_containing_object: List[Predicate]
    ) -> Optional[EmbeddedConstruction]:
        for pattern in CONSTRUCTION_PATTERNS:
            try:
                construction = pattern.match(object_, predicates_containing_object)
                if construction is not None:
                    return construction
            except UndefinedEmbeddingError:
                pass
        else:
            return None
    
    def process_assumptions(self, predicates: List[Predicate]) -> Optional[List[Predicate]]:
        processed_predicates = []
        for pred in predicates:
            # Removing open predicates:
            if pred.is_open():
                continue
            # Splitting all "Line(A, B) == l" and "Circle(A, B, C) == c" predicates into pieces:
            if pred.name == 'equals':
                lhs, rhs = pred.components
                if isinstance(rhs, ConstructionObject) and rhs.constructor.name in ['Line', 'Circle']:
                    lhs, rhs = rhs, lhs
                if isinstance(lhs, ConstructionObject) and lhs.constructor.name in ['Line', 'Circle']:
                    for point in lhs.components:
                        processed_predicates.append(predicate_from_args('in', (point, rhs)))
                    continue
            # Splitting all `In` predicates into pieces:
            if pred.name == 'in':
                point_indices = [i for i in range(len(pred.components)) if pred.components[i].type == POINT]
                curve_indices = [i for i in range(len(pred.components)) if pred.components[i].type != POINT]
                for i in point_indices:
                    for j in curve_indices:
                        if i >= j:
                            return None
                        processed_predicates.append(predicate_from_args('in', (pred.components[i], pred.components[j])))
                continue
            processed_predicates.append(pred)
        return processed_predicates

    def sequence_assumptions(self, objects: List[GeoObject], predicates: List[Predicate]) -> Optional[List[EmbeddedConstruction]]:
        constructions: List[EmbeddedConstruction] = []

        while len(objects) > 0:
            for object_ in list(objects):
                predicates_containing_object = [
                    predicate
                    for predicate in predicates
                    if any([obj.name == object_.name for obj in predicate.involved_objects()])
                ]
                construction = self.try_sequence_object(object_, predicates_containing_object)
                if construction is not None:
                    constructions.insert(0, construction)
                    for predicate in predicates_containing_object:
                        predicates.remove(predicate)
                    objects.remove(object_)
                    break
            else:
                return None

        return constructions

    def get_distinct_names(self, proof: Proof) -> Mapping[str, List[str]]:
        predicates = proof.assumption_predicates + proof.auxiliary_predicates
        distinct_names: Dict[str, List[str]] = defaultdict(list)
        for predicate in predicates:
            if isinstance(predicate, DistinctPredicate):
                for obj0, obj1 in itertools.combinations(predicate.components, 2):
                    distinct_names[obj0.name].append(obj1.name)
                    distinct_names[obj1.name].append(obj0.name)
        return distinct_names
    
    def embed_construction_sequence(self, constructions: List[EmbeddedConstruction], distinct_names: Mapping[str, List[str]]) -> Optional[Embedding]:
        embedding = Embedding()
        constructions = constructions[:]
        while len(constructions) > 0:
            for construction in list(constructions):
                try:
                    embedded_object_options = construction.construct(embedding, distinct_names)
                    ### TODO: What if there are multiple options?? What do???
                    if len(embedded_object_options) > 0:
                        embedding[construction.output_name] = embedded_object_options[0]
                        constructions.remove(construction)
                        break
                except:
                    pass
            else:
                return None
        return embedding
    
    def check_predicates(self, embedding: Embedding, predicates: List[Predicate]) -> bool:
        for pred in predicates:
            if embedding.evaluate_predicate(pred) != EmbeddedPredicateValue.Correct:
                return False
        else:
            return True

    def embed(self, proof: Proof) -> Optional[Embedding]:
        objects = list(proof.assumption_objects.values())
        separated_predicates = self.process_assumptions(proof.assumption_predicates)
        constructions = self.sequence_assumptions(objects, separated_predicates)

        if constructions is None:
            return None

        distinct_names: Mapping[str, List[str]] = self.get_distinct_names(proof)

        for _ in range(EMBEDDING_ATTEMPTS):
            embedding = self.embed_construction_sequence(constructions, distinct_names)
            if embedding is None:
                continue
            if not self.check_predicates(embedding, proof.assumption_predicates):
                continue
            return embedding
        return None


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Embeds problems in 2D Euclidean space.')
    parser.add_argument('path', help='The path of the problem file to embed.', type=Path)
    parser.add_argument(
        '--show',
        help='Print the embedding when successful.',
        action='store_true',
    )
    parser.add_argument(
        '--overwrite',
        help='Overwrite the file with the proof when embedding is complete.',
        action='store_true',
    )

    args = parser.parse_args()

    path = Proof.get_full_proof_path(args.path)
    proof = Proof.parse(path.open().read(), False)

    diagram_embedder = DiagramEmbedder()
    embedding = diagram_embedder.embed(proof)

    if embedding is None:
        print('Embedding failed')
        return
    
    proof.embedding = embedding

    proof_text = proof.to_language_format()

    if args.show:
        print(proof_text)

    if args.overwrite:
        open(path, 'w').write(proof_text)
    
    failed_predicates = [pred for pred in proof.target_predicates if embedding.evaluate_predicate(pred) == EmbeddedPredicateValue.Incorrect]
    unknown_predicates = [pred for pred in proof.target_predicates if embedding.evaluate_predicate(pred) == EmbeddedPredicateValue.Undefined]
    
    print('Embedding successful.')
    if len(failed_predicates) > 0:
        print('Incorrect target predicates:')
        for pred in failed_predicates:
            print(pred.to_language_format())
        print()
        
    if len(unknown_predicates) > 0:
        print('Unknown target predicates:')
        for pred in unknown_predicates:
            print(pred.to_language_format())
        print()
