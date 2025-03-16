from pathlib import Path
from typing import Iterator, List, Optional
from tqdm import tqdm

from ...rule_utils import LITERAL
from ...embeddings.undefined_embedding_error import UndefinedEmbeddingError
from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_trackers.geometry_tracker import GeometryTracker
from ...interactive_predicate_checker import InteractivePredicateChecker
from ...predicates.predicate import Predicate
from ...proof import Proof
from ...proof_gen.proof_generator import ProofGenerator, ProofGeneratorError, ProofGeneratorErrorType

from .. import Embedding
from ..embedded_objects import EmbeddedObject
from ..embedded_predicate_value import EmbeddedPredicateValue

from .construction_patterns.implementations import CONSTRUCTION_PATTERNS
from .embedded_constructions.embedded_construction import EmbeddedConstruction
from .sequencing_preprocessor.sequencing_preprocessor import SequencingPreprocessor


EMBEDDING_ATTEMPTS = 5


class DiagramEmbedder:
    def is_assumption_necessary(self, assumption: Predicate, assumptions: List[Predicate]) -> bool:
        try:
            objects = {
                obj.name: obj for pred in assumptions for obj in pred.involved_objects()
                if not isinstance(obj, ConstructionObject)
            }
            proof = Proof(
                objects, objects,
                assumptions, [],
                {}, [assumption],
                None, []
            )
            proof_gen = ProofGenerator(proof, actions_per_step=10000)
            proof_gen.run(1000)
            return False
        except ProofGeneratorError as e:
            if e.error in [ProofGeneratorErrorType.NoMoreSteps, ProofGeneratorErrorType.StepLimitReached]:
                return True
            else:
                raise
            
    def remove_necessary_assumptions(self, assumptions: List[Predicate]) -> List[Predicate]:
        necessary_assumptions = []
        for assumption in tqdm(assumptions):
            if self.is_assumption_necessary(assumption, necessary_assumptions):
                necessary_assumptions.append(assumption)
        return necessary_assumptions

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

    def sequence_assumptions(self, objects: List[GeoObject], predicates: List[Predicate]) -> Optional[List[EmbeddedConstruction]]:
        predicates = predicates[:]
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

    def embed_construction_sequence(self, constructions: List[EmbeddedConstruction], predicates_by_step: List[List[Predicate]]) -> Iterator[Embedding]:
        stage = 0
        construction_options: List[List[EmbeddedObject]] = []
        embedding = Embedding()
        while True:
            if stage < 0:
                return None
            elif stage == len(constructions):
                yield embedding.shallow_copy()
                stage -= 1
            elif stage == len(construction_options):
                options = []
                try:
                    options = list(constructions[stage].construct(embedding))
                except UndefinedEmbeddingError:
                    pass
                construction_options.append(options)
            elif len(construction_options[stage]) == 0:
                del construction_options[stage]
                stage -= 1
            else:
                options = construction_options[stage]
                while len(options) > 0:
                    embedding[constructions[stage].output_name] = options.pop()
                    for predicate in predicates_by_step[stage]:
                        if embedding.evaluate_predicate(predicate) != EmbeddedPredicateValue.Correct:
                            del embedding[constructions[stage].output_name]
                            break
                    else:
                        break
                if constructions[stage].output_name in embedding.keys():
                    stage += 1
                else:
                    del construction_options[stage]
                    stage -= 1

    def check_predicates(self, embedding: Embedding, predicates: List[Predicate]) -> bool:
        for pred in predicates:
            if embedding.evaluate_predicate(pred) != EmbeddedPredicateValue.Correct:
                return False
        else:
            return True

    def embed(self, proof: Proof) -> Optional[Embedding]:
        objects = list(proof.assumption_objects.values())
        preprocessor = SequencingPreprocessor()
        processed_predicates = preprocessor.preprocess_assumptions(proof.assumption_predicates)
        processed_predicates = self.remove_necessary_assumptions(processed_predicates)
        
        constructions = self.sequence_assumptions(objects, processed_predicates)

        if constructions is None:
            return None

        predicates_by_step = [[] for i in range(len(constructions))]
        name_to_stage = {construction.output_name: i for (i, construction) in enumerate(constructions)}
        for predicate in proof.assumption_predicates:
            involved_names = [obj.name for obj in predicate.involved_objects() if not isinstance(obj, ConstructionObject) and not obj.type == LITERAL]
            stage = max([name_to_stage[name] for name in involved_names])
            predicates_by_step[stage].append(predicate)

        for _ in tqdm(range(EMBEDDING_ATTEMPTS)):
            for embedding in self.embed_construction_sequence(constructions, predicates_by_step):
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
    parser.add_argument(
        '--interactive',
        help='Runs an interactive object and predicate evaluator if the embedding fails.',
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
        
    if len(failed_predicates) > 0 or len(unknown_predicates) > 0:
        print('Beginning interactive session...')
        geometry_tracker = GeometryTracker()
        geometry_tracker.load_assumptions(proof)
        geometry_tracker.load_embeds(proof)
        InteractivePredicateChecker(geometry_tracker).run()
