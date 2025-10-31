""" The Differences between Treescript Files.
"""
from typing import Generator

from treescript_files import generate_treescript_files


def diff_trees_additions(a: str, b: str) -> Generator[str, None, None]:
    """ The TreeScript files that were added from a to b.

**Parameters:**
 - a (str): The original TreeScript.
 - b (str): The updated TreeScript.

**Yields:**
 str - The elements of the diff that are added.
    """
    yield from _compare_files(_load_original(a), b)


def diff_trees_removals(a: str, b: str) -> Generator[str, None, None]:
    """ The TreeScript files that were removed from a to b.

**Parameters:**
 - a (str): The original TreeScript.
 - b (str): The updated TreeScript.

**Yields:**
 Generator[str] - The elements of the diff that were removed.
    """
    yield from diff_trees_additions(b, a)


def diff_trees_double(a: str, b: str) -> tuple[list[str], list[str]]:
    """ The difference between two TreeScript strings.

**Parameters:**
 - a (str): The original TreeScript.
 - b (str): The updated TreeScript.

**Returns:**
 tuple[list[str], list[str]] - Container for the additions and removals.
    """
    files: set[str] = _load_original(a)
    additions: list[str] = []
    additions.extend(_compare_files(files, b))
    removals: list[str] = []
    removals.extend(files)
    return additions, removals


def _load_original(
    original_treescript: str,
) -> set[str]:
    return set[str](generate_treescript_files(original_treescript, None))


def _compare_files(
    original_files: set[str],
    updated_tree: str
) -> Generator[str, None, None]:
    """ Compare a set of the original files with the updated TreeScript.
 - Modifies the original_files set during execution, removing matches with updated_tree.

**Parameters:**
 - original_files (set): The Dictionary containing the original TreeScript files.
 - updated_tree (str): The updated TreeScript to be compared for additions.

**Yields:**
 str - The file paths that were not found in the original TreeScript.
    """
    for node in generate_treescript_files(updated_tree, None):
        if node in original_files:
            original_files.remove(node)
        else:
            yield node
