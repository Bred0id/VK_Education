class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallestBST(root, k):
    stack = []
    counter = 0
    current = root
    while len(stack) > 0 or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val
        current = current.right
    return None

def kthLargestBST(root, k):
    stack = []
    counter = 0
    current = root
    while len(stack) > 0 or current is not None:
        while current is not None:
            stack.append(current)
            current = current.right
        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val
        current = current.left
    return None