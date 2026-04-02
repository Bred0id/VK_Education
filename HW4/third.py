class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    if root.left is not None:
        return 1 + minDepth(root.left)
    if root.right is not None:
        return 1 + minDepth(root.right)