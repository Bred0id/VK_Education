import pytest
from first import binarySearchSqrt
from second import copyTime
from third import feedAnimals
from fourth import extraLetter
from fiveth import twoSum


def test_binary_search_sqrt():
    assert binarySearchSqrt(0) == 0
    assert binarySearchSqrt(1) == 1
    assert binarySearchSqrt(2) == 1
    assert binarySearchSqrt(3) == 1
    assert binarySearchSqrt(4) == 2
    assert binarySearchSqrt(15) == 3
    assert binarySearchSqrt(16) == 4
    assert binarySearchSqrt(17) == 4
    assert binarySearchSqrt(25) == 5
    assert binarySearchSqrt(26) == 5
    assert binarySearchSqrt(100) == 10
    assert binarySearchSqrt(101) == 10
    assert binarySearchSqrt(10000) == 100
    assert binarySearchSqrt(10001) == 100


def test_copy_time():
    assert copyTime(1, 1, 2) == 1
    assert copyTime(2, 1, 2) == 2
    assert copyTime(3, 1, 2) == 3
    assert copyTime(4, 1, 2) == 3
    assert copyTime(5, 1, 2) == 4
    assert copyTime(10, 3, 3) == 18
    assert copyTime(1, 5, 10) == 5


def test_feed_animals():
    assert feedAnimals([3, 4, 7], [8, 1, 2]) == 1
    assert feedAnimals([3, 8, 1, 4], [1, 1, 2]) == 1
    assert feedAnimals([1, 2, 2], [7, 1]) == 2
    assert feedAnimals([8, 2, 3, 2], [1, 4, 3, 8]) == 3
    assert feedAnimals([], [1, 2, 3]) == 0
    assert feedAnimals([1, 2], []) == 0
    assert feedAnimals([], []) == 0
    assert feedAnimals([1, 2, 3], [3, 2, 1]) == 3
    assert feedAnimals([1, 1, 1], [1, 1, 1]) == 3
    assert feedAnimals([2, 2], [5, 5, 5]) == 2
    assert feedAnimals([10, 20], [5, 15]) == 1


def test_extra_letter():
    assert extraLetter("uio", "oeiu") == "e"
    assert extraLetter("fe", "efo") == "o"
    assert extraLetter("ab", "ab") == ""
    assert extraLetter("bbb", "bbbb") == "b"
    assert extraLetter("abc", "abcd") == "d"
    assert extraLetter("a", "aa") == "a"
    assert extraLetter("abcd", "abcde") == "e"
    assert extraLetter("aab", "aabb") == "b"
    assert extraLetter("aabb", "aabbb") == "b"


def test_two_sum():
    arr = [2, 7, 11, 15]
    indices = twoSum(arr, 9)
    assert len(indices) == 2
    assert indices[0] != indices[1]
    assert arr[indices[0]] + arr[indices[1]] == 9

    arr = [3, 2, 4]
    indices = twoSum(arr, 6)
    assert len(indices) == 2
    assert indices[0] != indices[1]
    assert arr[indices[0]] + arr[indices[1]] == 6

    arr = [3, 3]
    indices = twoSum(arr, 6)
    assert len(indices) == 2
    assert indices[0] != indices[1]
    assert arr[indices[0]] + arr[indices[1]] == 6

    assert twoSum([1, 2, 3], 7) == []

    arr = [-1, -2, -3, -4]
    indices = twoSum(arr, -5)
    assert len(indices) == 2
    assert indices[0] != indices[1]
    assert arr[indices[0]] + arr[indices[1]] == -5

    assert twoSum([5], 5) == []

    arr = [1, 5, 3, 9, 2]
    indices = twoSum(arr, 10)
    assert len(indices) == 2
    assert indices[0] != indices[1]
    assert arr[indices[0]] + arr[indices[1]] == 10