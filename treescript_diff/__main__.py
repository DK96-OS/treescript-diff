#!/usr/bin/python


def main():
    # Author: DK96-OS 2024 - 2025
    from sys import argv
    from treescript_diff.input import validate_arguments
    input_data = validate_arguments(argv[1:])
    #
    from treescript_diff import ts_diff
    print(ts_diff(input_data))


if __name__ == "__main__":
    from sys import path
    from pathlib import Path
    # Get the directory of the current file (__file__ is the path to the script being executed)
    # Add the directory to sys.path
    path.append(str(Path(__file__).resolve().parent.parent))
    main()
