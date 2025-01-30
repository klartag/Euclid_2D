from collections import defaultdict
import itertools
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence

from rules.proof import Proof

from ...geometry_objects.geo_object import GeoObject
from ...predicates.predicate import Predicate
from ...predicates.implementations.distinct_predicate import DistinctPredicate
from ...predicates.implementations.exists_predicate import ExistsPredicate

from ..embedded_objects import Embedding

from .construction_patterns.implementations import CONSTRUCTION_PATTERNS
from .embedded_constructions.embedded_construction import EmbeddedConstruction


class DiagramEmbedder:
    def try_sequence_object(
        self, object_: GeoObject, predicates_containing_object: List[Predicate]
    ) -> Optional[EmbeddedConstruction]:
        for pattern in CONSTRUCTION_PATTERNS:
            construction = pattern.match(object_, predicates_containing_object)
            if construction is not None:
                return construction
        else:
            return None

    def sequence_assumptions(
        self, proof: Proof
    ) -> Optional[List[EmbeddedConstruction]]:
        objects = list(proof.assumption_objects.values())
        predicates = [pred for pred in proof.assumption_predicates if not isinstance(pred, (DistinctPredicate, ExistsPredicate))]

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

    def embed(self, proof: Proof) -> Optional[Embedding]:
        constructions = self.sequence_assumptions(proof)

        if constructions is None:
            return None

        distinct_names: Mapping[str, List[str]] = self.get_distinct_names(proof)

        embedded_objects: Embedding = {}

        while len(constructions) > 0:
            for construction in list(constructions):
                try:
                    embedded_object = construction.construct(embedded_objects, distinct_names)
                    if embedded_object is not None:
                        embedded_objects[construction.output_name] = embedded_object
                        constructions.remove(construction)
                        break
                    else:
                        pass
                except:
                    pass
            else:
                return None

        return embedded_objects


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Embeds problems in 2D Euclidean space.')
    parser.add_argument('path', help='The path of the problem file to embed.', type=Path)
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
    
    if embedding is not None:
        proof.embedding = embedding
    
    proof_text = proof.to_language_format()
    if args.overwrite:
        open(path, 'w').write(proof_text)
    else:
        print(proof_text)
