class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root):
    if root is None:
        return True
    queue = [root]
    seenNull = False
    while len(queue) > 0:
        node = queue.pop(0)
        if node is None:
            seenNull = True
        else:
            if seenNull:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True