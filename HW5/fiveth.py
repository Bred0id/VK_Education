class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balanceFactor = 0

def calculateHeightsAndBalance(node):
    if node is None:
        return 0
    leftHeight = calculateHeightsAndBalance(node.left)
    rightHeight = calculateHeightsAndBalance(node.right)
    node.balanceFactor = leftHeight - rightHeight
    return 1 + max(leftHeight, rightHeight)