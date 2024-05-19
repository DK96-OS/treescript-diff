"""The Arguments Received from the Command Line Input.

This DataClass is created after the argument syntax is validated.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentData:
    """
    The syntactically valid arguments received by the Program.

    Fields:
    - original (str) : The initial TreeScript.
    - updated (str): The updated TreeScript.
    """

    original: str = True
    updated: str = True
