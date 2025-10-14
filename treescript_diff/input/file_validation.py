""" File Validation Methods.
 - These Methods all raise SystemExit exceptions.
"""
from pathlib import Path
from stat import S_ISLNK
from sys import exit

from treescript_diff.input import _validate_name


_FILE_SIZE_LIMIT = 8 * 1024**2 # 8 MB
_FILE_SIZE_LIMIT_ERROR_MSG = "File larger than 8 MB Limit."
_FILE_SYMLINK_DISABLED_MSG = "Symlink file paths are disabled."

_FILE_DOES_NOT_EXIST_MSG = "The File does not Exist."
_FILE_READ_OSERROR_MSG = "Failed to Read from File."


def validate_input_file(file_name: str) -> str | None:
    """ Read the Input File, Validate (non-blank) data, and return Input str.
 - Max FileSize is 8 MB.
 - Symlink type file paths are disabled.

**Parameters:**
 - file_name (str): The Name of the Input File.

**Returns:**
 str - The String Contents of the Input File.

**Raises:**
 SystemExit - If the File does not exist, or is empty or blank, or read failed.
    """
    file_path = Path(file_name)
    try:
        if not file_path.exists():
            exit(_FILE_DOES_NOT_EXIST_MSG)
        if S_ISLNK((stat := file_path.lstat()).st_mode):
            exit(_FILE_SYMLINK_DISABLED_MSG)
        if stat.st_size > _FILE_SIZE_LIMIT:
            exit(_FILE_SIZE_LIMIT_ERROR_MSG)
        if (data := file_path.read_text()) is not None:
            if _validate_name(data):
                return data
            exit(f"This TreeScript file was empty: {file_name}")
        # Fallthrough: return None
    except OSError:
        exit(_FILE_READ_OSERROR_MSG)
    return None
