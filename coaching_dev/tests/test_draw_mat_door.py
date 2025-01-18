import pytest
from io import StringIO
from contextlib import redirect_stdout
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_dev.door_mat import draw_mat_door

def test_draw_mat_door_valid_size():

    # Test for a valid odd size
    expected_output = (
        "------------.|.------------\n"
        "---------.|..|..|.---------\n"
        "------.|..|..|..|..|.------\n"
        "---.|..|..|..|..|..|..|.---\n"
        "----------WELCOME----------\n"
        "---.|..|..|..|..|..|..|.---\n"
        "------.|..|..|..|..|.------\n"
        "---------.|..|..|.---------\n"
        "------------.|.------------\n"
    )

    size = 9
    with StringIO() as buf, redirect_stdout(buf):
        draw_mat_door(size)
        output = buf.getvalue()

    assert output == expected_output

def test_draw_mat_door_invalid_size_even():

    # Test for an even size
    size = 8
    with pytest.raises(ValueError, match="Input must be an odd integer."):
        draw_mat_door(size)

def test_draw_mat_door_invalid_size_non_integer():

    # Test for a non-integer size
    size = "abc"
    with pytest.raises(ValueError, match="Input must be an odd integer."):
        draw_mat_door(size)

def test_draw_mat_door_edge_case_size_1():

    # Test for the smallest odd size (1)
    expected_output = "WELCOME\n"

    size = 1
    with StringIO() as buf, redirect_stdout(buf):
        draw_mat_door(size)
        output = buf.getvalue()

    assert output == expected_output

def test_draw_mat_door_large_size():

    # Test for a large odd size
    size = 11
    with StringIO() as buf, redirect_stdout(buf):
        draw_mat_door(size)
        output = buf.getvalue()

    # Verify the structure of the output
    lines = output.strip().split('\n')
    assert len(lines) == size  # The number of lines should match the size
    assert "WELCOME" in lines[size // 2]  # The middle line should contain 'WELCOME'
    assert lines[0].strip('-') == '.|.'  # The topmost pattern
    assert lines[-1].strip('-') == '.|.'  # The bottommost pattern
