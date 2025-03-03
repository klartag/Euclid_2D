import sys

from .proof_checker import main as proof_checker_main
from .proof_gen.proof_generator import validate_main as proof_validator_main
from .proof_gen.proof_generator import main as proof_generator_main
from .trimmers.old_trimmer import main as old_trimmer_main
from .trimmers.trimmer import main as trimmer_main
from .proof_prettifier import main as prettifier_main
from .pred_config import load_constructions_and_macros


HELP_MESSAGE = """\
*** 2D Euclid ***
The following commands are supported:

check [<args>]     -   Checks that a proof is correct.
validate [<args>]  -   Validates that the Proof Generator can create this proof.
prove [<args>]     -   Proves a Geometry problem.
trim [<args>]      -   Shortens a given proof.
prettify [<args>]  -   Makes a proof more readable for our neural net.

Specific arguments for each command are explained when provided with the `-h` flag.
For instance: `python -m rules prove -h`.
"""


PROGRAM_LIST = {
    'check': proof_checker_main,
    'validate': proof_validator_main,
    'prove': proof_generator_main,
    'old_trim': old_trimmer_main,
    'trim': trimmer_main,
    'prettify': prettifier_main,
}


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] not in PROGRAM_LIST:
        print(HELP_MESSAGE)
    else:
        load_constructions_and_macros()
        main = PROGRAM_LIST[sys.argv[1]]
        del sys.argv[1]
        main()
