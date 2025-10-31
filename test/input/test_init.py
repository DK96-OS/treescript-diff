"""Testing Input Package Methods
"""
import os

import pytest

from treescript_diff.input import validate_arguments
from treescript_diff.input.input_data import InputData


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (['origin', 'update'], InputData('src/', 'src/', None)),
        (['origin', 'update', '--added'], InputData('src/', 'src/', True)),
        (['origin', 'update', '-a'], InputData('src/', 'src/', True)),
        (['origin', 'update', '--removed'], InputData('src/', 'src/', False)),
        (['origin', 'update', '-r'], InputData('src/', 'src/', False)),
    ]
)
def test_validate_arguments_returns_input(tmp_path, test_input, expected):
    os.chdir(tmp_path)
    (origin_file := tmp_path / 'origin').touch()
    (update_file := tmp_path / 'update').touch()
    origin_file.write_text('src/')
    update_file.write_text('src/')
    assert validate_arguments(test_input) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        (['']),
        ([' ']),
        (['r']),
        (['eee']),
        (['e', '--add']),
        (['o', 'u', '--add', '-r']),
    ]
)
def test_validate_arguments_raises_exit(test_input):
    try:
        validate_arguments(test_input)
        assert False
    except SystemExit:
        assert True
