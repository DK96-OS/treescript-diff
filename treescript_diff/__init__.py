""" TreeScript Diff Methods.
"""
from treescript_diff.input.input_data import InputData
from treescript_diff.diff_trees import diff_trees_additions, diff_trees_double, diff_trees_removals


def ts_diff(data: InputData) -> str:
    """ TreeScript Diff entry point.

**Parameters:**
 - data (InputData): The program input data.

**Returns:**
 str - The output of the diff, formatted according to InputData options.
    """
    if data.diff_output is None:
        added, removed = diff_trees_double(data.original_tree, data.updated_tree)
        return "\n".join(added) + "\n\n" + "\n".join(removed)
    else:
        return "\n".join(
            (diff_trees_additions if data.diff_output else diff_trees_removals)
            (data.original_tree, data.updated_tree)
        )
