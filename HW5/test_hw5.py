import pytest
from first import isCompleteTree
from second import mergeKSortedArrays
from third import kthSmallest, kthLargest
from fourth import kthSmallestBST, kthLargestBST
from fiveth import calculateHeightsAndBalance
from sixth import mirrorTree
from zero import buildTree

def test_is_complete_tree():
    root = buildTree([1, 2, 3, 4, 5, 6])
    assert isCompleteTree(root) is True
    root2 = buildTree([1, 2, 3, None, 4])
    assert isCompleteTree(root2) is False
    assert isCompleteTree(None) is True

def test_merge_k_sorted_arrays():
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    assert mergeKSortedArrays(arrays) == [1, 1, 2, 3, 4, 4, 5, 6]
    arrays2 = [[1, 2, 3], [4, 5, 6], []]
    assert mergeKSortedArrays(arrays2) == [1, 2, 3, 4, 5, 6]
    assert mergeKSortedArrays([[], []]) == []

def test_kth_smallest_largest():
    arr = [3, 2, 1, 5, 6, 4]
    assert kthSmallest(arr, 2) == 2
    assert kthLargest(arr, 2) == 5
    assert kthSmallest([1], 1) == 1
    assert kthLargest([1], 1) == 1
    assert kthSmallest([], 1) is None
    assert kthLargest([], 1) is None
    assert kthSmallest([1,2], 3) is None
    assert kthLargest([1,2], 3) is None

def test_kth_in_bst():
    root = buildTree([5, 3, 6, 2, 4, None, 7])
    assert kthSmallestBST(root, 1) == 2
    assert kthSmallestBST(root, 3) == 4
    assert kthSmallestBST(root, 5) == 6
    assert kthSmallestBST(root, 6) == 7
    assert kthSmallestBST(root, 7) is None
    assert kthLargestBST(root, 1) == 7
    assert kthLargestBST(root, 2) == 6
    assert kthLargestBST(root, 5) == 3
    assert kthLargestBST(root, 6) == 2
    assert kthLargestBST(root, 7) is None
    assert kthSmallestBST(None, 1) is None
    assert kthLargestBST(None, 1) is None

def test_balance_factor():
    assert calculateHeightsAndBalance(None) == 0
    single = buildTree([42])
    calculateHeightsAndBalance(single)
    assert single.balanceFactor == 0
    root = buildTree([10, 5, 15, 3])
    calculateHeightsAndBalance(root)
    assert root.balanceFactor == 1
    assert root.left.balanceFactor == 1
    assert root.right.balanceFactor == 0

def test_mirror_tree():
    assert mirrorTree(None) is None
    single = buildTree([99])
    mirrored_single = mirrorTree(single)
    assert mirrored_single.val == 99
    assert mirrored_single.left is None
    assert mirrored_single.right is None
    root = buildTree([1, 2, 3])
    mirrored = mirrorTree(root)
    assert mirrored.val == 1
    assert mirrored.left.val == 3
    assert mirrored.right.val == 2