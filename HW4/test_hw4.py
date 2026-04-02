import pytest
from first import buildTree
from second import isSymmetric
from third import minDepth
from fourth import maxMinMultiplication
from fiveth import isSameTree

def test_build_tree():
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = buildTree(arr, 0)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7

def test_is_symmetric():
    arr = [1, 2, 2, 3, 4, 4, 3]
    root = buildTree(arr, 0)
    assert isSymmetric(root) is True
    arr2 = [1, 2, 2, None, 3, None, 3]
    root2 = buildTree(arr2, 0)
    assert isSymmetric(root2) is False
    assert isSymmetric(None) is True

def test_min_depth():
    root = buildTree([1], 0)
    assert minDepth(root) == 1
    root = buildTree([1, 2], 0)
    assert minDepth(root) == 2
    root = buildTree([1, 2, 3, 4, 5], 0)
    assert minDepth(root) == 2
    root = buildTree([1, 2, None, 3], 0)
    assert minDepth(root) == 3

def test_max_min_multiplication():
    arr = [16, 10, 19, 6, 12, 17, 21]
    assert maxMinMultiplication(arr) == 6 * 21
    assert maxMinMultiplication([1, 2]) == -1
    assert maxMinMultiplication([5]) == -1
    arr2 = [10, 5, 15]
    assert maxMinMultiplication(arr2) == 5 * 15

def test_is_same_tree():
    tree1 = buildTree([1, 2, 3], 0)
    tree2 = buildTree([1, 2, 3], 0)
    assert isSameTree(tree1, tree2) is True
    tree3 = buildTree([1, 2, None], 0)
    assert isSameTree(tree1, tree3) is False
    assert isSameTree(None, None) is True
    single = buildTree([1], 0)
    assert isSameTree(single, None) is False