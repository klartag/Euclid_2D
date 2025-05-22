from typing import Optional


def generic_split_args(text: str, separator_chars: str) -> Optional[tuple[list[str], list[str]]]:
    parenthesis_depth = 0
    split_indices = [-1]
    for i, c in enumerate(text):
        match c:
            case '(':
                parenthesis_depth += 1
            case ')':
                parenthesis_depth -= 1
                if parenthesis_depth < 0:
                    return None
            case _ if c in separator_chars:
                if parenthesis_depth == 0:
                    split_indices.append(i)
    if parenthesis_depth != 0:
        return None
    split_indices.append(len(text))

    args = [text[i + 1 : j].strip() for i, j in zip(split_indices, split_indices[1:])]
    separators = [text[i] for i in split_indices[1:-1]]

    return (args, separators)


def split_args(text: str) -> Optional[list[str]]:
    """
    Splits the given string using commas, while ignoring commas inside parentheses.
    """
    result = generic_split_args(text, ',')
    if result is None:
        return None
    return result[0]


def alternating_merge_string(lines0: list[str], lines1: list[str]) -> str:
    if len(lines0) < len(lines1):
        lines0.extend([''] * (len(lines1) - len(lines0)))
    if len(lines0) > len(lines1):
        lines1.extend([''] * (len(lines0) - len(lines1)))
    return ''.join([x + y for (x, y) in zip(lines0, lines1)])


def is_valid_parenthesis(text: str) -> bool:
    return generic_split_args(text[1:-1], '') is not None
