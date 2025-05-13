import sys

from .proof_checker import main as proof_checker_main, interactive_main
from .proof_gen.main import validate_main as proof_validator_main, main as proof_generator_main
from .trimmers.old_trimmer import main as old_trimmer_main
from .trimmers.new_trimmer import main as new_trimmer_main
from .embeddings.embedder.embedder import main as embedder_main
from .trimmers.trimmer import main as trimmer_main
from .proof_prettifier import main as prettifier_main
from .pred_config import load_constructions_and_macros


HELP_MESSAGE = """\
*** 2D Euclid ***
The following commands are supported:

embed [<args>]          -   Embeds the problem in 2D space.
check [<args>]          -   Checks that a proof is correct.
validate [<args>]       -   Validates that the Proof Generator can create this proof.
prove [<args>]          -   Proves a Geometry problem.
trim [<args>]           -   Shortens a given proof.
new_trim [<args>]       -   Shortens a given proof with the new trimmer.
prettify [<args>]       -   Makes a proof more readable for our neural net.
interactive [<args>]    -   Loads the proof into an interactive checker.

Specific arguments for each command are explained when provided with the `-h` flag.
For instance: `python -m rules prove -h`.
"""

PROGRAM_LIST = {
    'embed': embedder_main,
    'check': proof_checker_main,
    'validate': proof_validator_main,
    'prove': proof_generator_main,
    'old_trim': old_trimmer_main,
    'trim': trimmer_main,
    'new_trim': new_trimmer_main,
    'prettify': prettifier_main,
    'interactive': interactive_main,
}


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] not in PROGRAM_LIST:
        print(HELP_MESSAGE)
    else:
        load_constructions_and_macros()
        main = PROGRAM_LIST[sys.argv[1]]
        del sys.argv[1]
        main()
