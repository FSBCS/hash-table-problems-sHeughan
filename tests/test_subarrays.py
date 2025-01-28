import pytest
from p3 import count_subarrays_with_sum

def test_basic():
    assert count_subarrays_with_sum([1, 1, 1], 2) == 2

def test_basic_2():
    assert count_subarrays_with_sum([1, 2, 3], 3) == 2

def test_basic_3():
    assert count_subarrays_with_sum([1, -1, 1, 1, 1], 2) == 4

def test_single_element():
    assert count_subarrays_with_sum([1], 1) == 1

def test_empty_list():
    assert count_subarrays_with_sum([], 0) == 0

def test_no_subarrays():
    assert count_subarrays_with_sum([1, 2, 3], 7) == 0

def test_negative_numbers():
    assert count_subarrays_with_sum([-1, -1, 1], 0) == 1
