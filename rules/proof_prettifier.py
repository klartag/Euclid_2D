from pathlib import Path
from typing import List

from rules.proof.document.document_section import DocumentSection
from rules.proof.document.writer.document_writer import DocumentWriter

from .theorem import Theorem
from .proof.document.geometry_document import GeometryDocument
from .proof.document.reader.document_reader import DocumentReader
from .proof.proof import Proof
from .proof.steps import AssertStep, TheoremStep


class ProofPrettifier:
    def __init__(self):
        pass

    def prettify(self, proof: Proof) -> Proof:
        pretty_steps = []

        for step in proof.steps:
            if isinstance(step, TheoremStep):
                for assert_step in self.generate_assert_steps(step):
                    pretty_steps.append(assert_step)

            pretty_steps.append(step)

        pretty_proof = proof.shallow_copy()
        pretty_proof.steps = pretty_steps

        return pretty_proof

    def generate_assert_steps(self, step: TheoremStep) -> List[AssertStep]:
        theorem = Theorem.from_name(step.theorem_name)

        substitutions = {
            theorem_parameter: theorem_argument
            for theorem_parameter, theorem_argument in zip(theorem.signature, step.inputs)
        }

        return [AssertStep([predicate.substitute(substitutions)]) for predicate in theorem.required_predicates]


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Makes proofs more readable for our neural net.')
    parser.add_argument('path', help='The path of the proof file to prettify.', type=Path)
    parser.add_argument(
        '--overwrite',
        help='Overwrite the file with the prettified proof when prettifying is complete.',
        action='store_true',
    )

    args = parser.parse_args()
    document = GeometryDocument(args.path)
    problem = DocumentReader().read(document, read_proof_body=True)

    prettifier = ProofPrettifier()
    problem.proof = prettifier.prettify(problem.proof)

    DocumentWriter().write_sections(problem, document, DocumentSection.PROOF)
    if args.overwrite:
        document.save()
    else:
        for line in document.get_section_content(DocumentSection.PROOF):
            print(line)
