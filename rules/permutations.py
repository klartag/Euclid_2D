from typing import List, Optional, TypeVar

T = TypeVar('T')


def try_match_permutation(source_list: List[T], destination_list: List[T]) -> Optional[List[int]]:
    """
    Given two lists, tries to find a permutation that turns one list into the other.
    
    If no permutation can be found, returns None.
    Otherwise, returns a permutation `permutation_indices`, that satisfies
    
    destination_list[permutation_indices[i]] = source_list[i]
    """
    destination_list = destination_list[:]
    
    if len(source_list) != len(destination_list):
        return None

    indices = list(range(len(source_list)))
    permutation_indices: list[int] = []

    for value in source_list:
        if value not in destination_list:
            return None
        index = destination_list.index(value)
        permutation_indices.append(indices[index])
        del destination_list[index]
        del indices[index]

    return permutation_indices
