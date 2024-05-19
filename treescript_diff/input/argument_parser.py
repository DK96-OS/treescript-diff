"""Defines and Validates Argument Syntax.

Encapsulates Argument Parser.

Returns Argument Data, the args provided by the User.
"""
from argparse import ArgumentParser
from sys import exit
from typing import Optional

from .argument_data import ArgumentData
from .string_validation import validate_name


def parse_arguments(args: Optional[list[str]] = None) -> ArgumentData:
    """
    Parse command line arguments.

    Parameters:
    - args: A list of argument strings.

    Returns:
    ArgumentData : Container for Valid Argument Data.
    """
    if args is None or len(args) == 0:
        exit("No Arguments given. ")
    # Initialize the Parser and Parse Immediately
    try:
        parsed_args = _define_arguments().parse_args(args)
    except SystemExit as e:
        exit("Unable to Parse Arguments.")
    #
    return _validate_arguments(
        parsed_args.original,
        parsed_args.updated,
    )


def _validate_arguments(
    original: str,
    updated: str,
) -> ArgumentData:
    """
    Checks the values received from the ArgParser.
        Uses Validate Name method from StringValidation.

    Parameters:
    - original (str): The name of the original file
    - updated (str): The name of the updated file

    Returns:
    ArgumentData - A DataClass of syntactically correct arguments.
    """
    if not validate_name(original):
        exit("The original argument was invalid.")
    if not validate_name(updated):
        exit("The updated argument was invalid.")
    return ArgumentData(
        original=original,
        updated=updated,
    )


def _define_arguments() -> ArgumentParser:
    """
    Initializes and Defines Argument Parser.
       - Sets Required/Optional Arguments and Flags.

    Returns:
    argparse.ArgumentParser - An instance with all supported Arguments.
    """
    parser = ArgumentParser(
        description="Tree Script Builder"
    )
    # Required arguments
    parser.add_argument(
        'original',
        type=str,
        help='The original TreeScript.'
    )
    parser.add_argument(
        'updated',
        type=str,
        help='The updated TreeScript.',
    )
    return parser
