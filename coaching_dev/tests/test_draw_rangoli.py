import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_dev.rango_alpha import draw_rangoli

def test_draw_rangoli_size_1():
    expected = "a"
    assert draw_rangoli(1) == expected


def test_draw_rangoli_size_2():
    expected = "--b--\n" \
               "b-a-b\n" \
               "--b--"
    assert draw_rangoli(2) == expected


def test_draw_rangoli_size_3():
    expected = "----c----\n" \
               "--c-b-c--\n" \
               "c-b-a-b-c\n" \
               "--c-b-c--\n" \
               "----c----"
    assert draw_rangoli(3) == expected


def test_draw_rangoli_size_4():
    expected = "------d------\n" \
               "----d-c-d----\n" \
               "--d-c-b-c-d--\n" \
               "d-c-b-a-b-c-d\n" \
               "--d-c-b-c-d--\n" \
               "----d-c-d----\n" \
               "------d------"
    assert draw_rangoli(4) == expected


def test_draw_rangoli_size_5():
    expected = "--------e--------\n" \
               "------e-d-e------\n" \
               "----e-d-c-d-e----\n" \
               "--e-d-c-b-c-d-e--\n" \
               "e-d-c-b-a-b-c-d-e\n" \
               "--e-d-c-b-c-d-e--\n" \
               "----e-d-c-d-e----\n" \
               "------e-d-e------\n" \
               "--------e--------"
    assert draw_rangoli(5) == expected


def test_draw_rangoli_large_size():
    result = draw_rangoli(10)
    assert len(result.splitlines()) == 19
    assert result.startswith("------------------j------------------")
    assert result.endswith("------------------j------------------")
