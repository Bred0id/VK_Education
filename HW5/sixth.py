class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirrorTree(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    mirrorTree(node.left)
    mirrorTree(node.right)
    return node