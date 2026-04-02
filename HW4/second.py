class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deptSearch(root, res):
    if root is None:
        return res
    deptSearch(root.left, res)
    res.append(root.val)
    deptSearch(root.right, res)
    return res

def isSymmetric(root):
    if root is None:
        return True
    data = []
    data = deptSearch(root, data)
    for i in range(len(data) // 2):
        if data[i] != data[-i - 1]:
            return False
    return True