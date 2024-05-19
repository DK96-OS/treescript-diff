"""TreeScript Diff Methods
"""
from .input.input_data import InputData
from .diff_trees import diff_trees_additions


def ts_diff(data: InputData) -> str:
    """
    """
    new_files = diff_trees_additions(
        data.original_tree,
        data.updated_tree,
    )
    # This flag will return the file paths.
    return "\n".join(new_files)
