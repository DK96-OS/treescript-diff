""" The methods of a dictionary-files based diff algorithm.
"""
from typing import Generator

from treescript_files.input_data import InputData
from treescript_files.tree_reader import process_input_data


def load_original(original_tree: str) -> set[str]:
    """ Convert Original TreeScript into Files, and add them to a set.

**Parameters:**
 - original_tree (str): The original TreeScript.

**Returns:**
 set[str] - A set containing files.
    """
    files: set[str] = set[str]()
    # This is InputData to the TreeScript Files external Package
    files_input_data = InputData(
        tree_input=original_tree,
        parent_path=None
    )
    for node in process_input_data(files_input_data):
        files.add(node)
    return files


def compare_files(
    original_files: set[str],
    updated_tree: str
) -> Generator[str, None, None]:
    """ Compare a set of the original files with the updated TreeScript.

**Parameters:**
 - original_files (set) : The Dictionary containing the original TreeScript files.
 - updated_tree (str) : The updated TreeScript to be compared for additions.

**Yields:**
 str[str] - The file paths.
    """
    files_input_data = InputData(
        tree_input=updated_tree,
        parent_path=None
    )
    for node in process_input_data(files_input_data):
        if node in original_files:
            original_files.remove(node)
        else:
            yield node
