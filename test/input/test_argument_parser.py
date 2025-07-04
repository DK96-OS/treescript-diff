""" Testing Argument Parser Methods.
"""
import pytest

from treescript_diff.input.argument_data import ArgumentData
from treescript_diff.input.argument_parser import parse_arguments


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (['origin', 'update'], ArgumentData('origin', 'update', None)),
        (['origin', 'update', '--add'], ArgumentData('origin', 'update', True)),
        (['origin', 'update', '-a'], ArgumentData('origin', 'update', True)),
        (['origin', 'update', '--removed'], ArgumentData('origin', 'update', False)),
        (['origin', 'update', '-r'], ArgumentData('origin', 'update', False)),
    ]
)
def test_parse_arguments_returns_input(test_input, expected):
	assert parse_arguments(test_input) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        ([]),
        (['']),
        ([' ']),
        (['r']),
        (['origin', '']),
        (['', 'updated']),
        (['origin', 'updated', '--unknown']),
    ]
)
def test_parse_arguments_raises_exit(test_input):
	with pytest.raises(SystemExit):
		parse_arguments(test_input)
        

def test_parse_arguments_both_added_and_removed_raises_exit():
	with pytest.raises(SystemExit, match='Added and Removed files are printed by default, separated by a blank line.'):
		parse_arguments(['origin', 'updated', '-ar'])
