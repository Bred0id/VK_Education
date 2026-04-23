import pytest
from first import find_length_of_lcis
from second import generate_pascal_triangle
from third import coin_change
from fourth import longest_palindrome

def test_first():
    assert find_length_of_lcis([3, 2, 8, 9, 5, 10]) == 3
    assert find_length_of_lcis([1, 2, 7, 9, 0, 10]) == 4
    assert find_length_of_lcis([8, 8, 8, 8]) == 1
    assert find_length_of_lcis([]) == 0
    assert find_length_of_lcis([1, 2, 3, 4, 5]) == 5
    assert find_length_of_lcis([5, 4, 3, 2, 1]) == 1

def test_second():
    assert generate_pascal_triangle(0) == []
    assert generate_pascal_triangle(1) == [[1]]
    assert generate_pascal_triangle(2) == [[1], [1, 1]]
    assert generate_pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]
    expected_6 = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
    assert generate_pascal_triangle(6) == expected_6

def test_third():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([5, 10], 3) == -1
    assert coin_change([3], 9) == 3
    assert coin_change([1, 3, 4], 6) == 2
    assert coin_change([1, 3, 4], 10) == 3

def test_fourth():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("") == ""
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("abba") == "abba"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("noon") == "noon"
    assert longest_palindrome("abcdef") in "abcdef"
    assert longest_palindrome("aaaaa") == "aaaaa"