import pytest
from first import max_sum_subarray_k
from second import subarray_sum_equals_k
from third import find_max_length
from fourth_from_seminar import pivot_index
from fourth_from_task import find_rotation_point
from fifth import is_balanced_parentheses

def test_first():
    assert max_sum_subarray_k([3, 2, 8, 9, 5, 10], 3) == 24
    assert max_sum_subarray_k([1, 2, 7, 9, 0, 10], 4) == 26
    assert max_sum_subarray_k([8, 8, 8, 8], 2) == 16
    assert max_sum_subarray_k([5], 1) == 5
    assert max_sum_subarray_k([], 2) is None
    assert max_sum_subarray_k([1, 2], 3) is None

def test_second():
    assert subarray_sum_equals_k([3, 8, 6, 9, 2, 1, 4], 11) == 2
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2
    assert subarray_sum_equals_k([0, 0, 0], 0) == 6
    assert subarray_sum_equals_k([], 5) == 0

def test_third():
    assert find_max_length([0, 1, 0, 0, 1]) == 4
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 0, 1, 1, 1]) == 4
    assert find_max_length([1, 1, 1, 1]) == 0
    assert find_max_length([]) == 0

def test_fourth_from_seminar():
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
    assert pivot_index([0, 0, 0, 0]) == 0
    assert pivot_index([]) == -1

def test_fourth_from_task():
    assert find_rotation_point([4, 5, 6, 7, 0, 1, 2]) == 4
    assert find_rotation_point([11, 13, 15, 17]) == 0
    assert find_rotation_point([2, 2, 2, 0, 1]) == 3
    assert find_rotation_point([1, 2, 3, 4, 5]) == 0
    assert find_rotation_point([]) == -1

def test_fifth():
    assert is_balanced_parentheses("()") is True
    assert is_balanced_parentheses("(()())") is True
    assert is_balanced_parentheses("(()") is False
    assert is_balanced_parentheses(")(") is False
    assert is_balanced_parentheses("") is True
    assert is_balanced_parentheses("(()))") is False