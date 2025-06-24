from collections import Counter
import glob
import argparse
from pathlib import Path
from glob import glob

from ..embeddings.embedder.embedder import DiagramEmbedder
from ..proof_prettifier import ProofPrettifier
from ..trimmers.trimmer import ProofTrimmer
from ..proof.steps import TheoremStep
from ..proof.document.document_section import DocumentSection
from ..proof.document.geometry_document import GeometryDocument
from ..proof.document.reader.document_reader import DocumentReader
from ..proof.document.writer.document_writer import DocumentWriter
from ..trimmers.trimmer import ProofTrimmer

from .proof_generator import validate_proof, prove


def validate_main():
    """
    TODO: Document
    """
    parser = argparse.ArgumentParser(
        description='''Tries to validate that a proof can be found by the proof generator,
without actually running the proof generator.'''
    )
    parser.add_argument('path')
    args = parser.parse_args()

    document = GeometryDocument.open(args.path)
    problem = DocumentReader().read(document, read_proof_body=False)
    validate_proof(problem)


def main():
    parser = argparse.ArgumentParser(description='Attempts to prove a Geometry problem.')
    parser.add_argument('path', help='The path of the problem to prove.', type=str)
    parser.add_argument(
        '--glob',
        help='Use this flag when the path argument is a glob\n\
        of paths. Runs the ProofGenerator seperately on each of these paths.',
        action='store_true',
    )
    parser.add_argument(
        '--interactive',
        help='When a proof fails due to NoMoreSteps or a KeyboardInterrupt, allows the user to check what was proved.',
        action='store_true',
    )
    parser.add_argument(
        '--overwrite',
        help='Overwrite the file with the proof when proving is complete.\n\
              (If `--trim` or `--prettify` are on, will overwrite the problem file\n\
              multiple times each time a step is completed)',
        action='store_true',
    )
    parser.add_argument(
        '--embed',
        help='If the proof has no embedding, runs it through the DiagramEmbedder.',
        action='store_true',
    )
    parser.add_argument(
        '--trim',
        help='Also runs the generated proof through the ProofTrimmer.',
        action='store_true',
    )
    parser.add_argument(
        '--prettify',
        help='Also runs the generated proof through the ProofPrettifier.',
        action='store_true',
    )
    parser.add_argument(
        '--ignore-errors',
        help='Only prints an error if it happens, without raising the exception.',
        action='store_true',
    )

    args = parser.parse_args()

    paths = [Path(p) for p in glob(args.path)] if args.glob else [args.path]

    if len(paths) == 0:
        print('No matching files found.')

    for i, path in enumerate(paths):
        if len(paths) > 1:
            print(f'[{i+1}/{len(paths)}] Proving file "{path}":')
        else:
            print(f'Proving file "{path}":')

        document = GeometryDocument.open(path)
        problem = DocumentReader().read(document, read_proof_body=True)

        try:
            if args.embed and problem.embedding is None:  # ARGS.embed
                print('Running Embedder...')
                diagram_embedder = DiagramEmbedder()
                problem.embedding = diagram_embedder.embed(problem)

                DocumentWriter().write_sections(problem, document, DocumentSection.EMBEDDING)
                if args.overwrite:
                    document.save()
                else:
                    for line in document.get_section_content(DocumentSection.EMBEDDING):
                        print(line)

            print('Running Prover...')
            problem = prove(problem, interactive=args.interactive, verbose=True)

            DocumentWriter().write_sections(problem, document, DocumentSection.PROOF)
            if args.overwrite:
                document.save()
            else:
                for line in document.get_section_content(DocumentSection.PROOF):
                    print(line)

            counter = Counter([x.theorem_name for x in problem.proof.steps if isinstance(x, TheoremStep)])
            if len(counter) > 0:
                longest_name = max(map(len, counter.keys()))
                for name, count in sorted(counter.items(), key=lambda x: x[1]):
                    print(f'{name:<{longest_name}}:', count)

            if args.trim:
                print('Running Trimmer...')
                trimmer = ProofTrimmer(problem)
                problem = trimmer.trim()

                DocumentWriter().write_sections(problem, document, DocumentSection.PROOF)
                if args.overwrite:
                    document.save()
                else:
                    for line in document.get_section_content(DocumentSection.PROOF):
                        print(line)

            if args.prettify:
                print('Running Prettifier...')
                prettifier = ProofPrettifier()
                problem.proof = prettifier.prettify(problem.proof)

                DocumentWriter().write_sections(problem, document, DocumentSection.PROOF)
                if args.overwrite:
                    document.save()
                else:
                    for line in document.get_section_content(DocumentSection.PROOF):
                        print(line)
        except KeyboardInterrupt as e:
            print(e)
            if i == len(paths) - 1:
                return
            user_input = ''
            while user_input.lower() not in ['s', 'q']:
                user_input = input("(S)kip or (Q)uit?")
            if user_input.lower() == 's':
                continue
            else:
                return
        except Exception if args.ignore_errors else NeverMatch as e:
            print('Error:', e)


class NeverMatch(Exception):
    pass
