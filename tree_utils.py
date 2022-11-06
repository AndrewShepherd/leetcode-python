class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(l: list, index = 0):
    if index >= len(l):
        return None
    return TreeNode(l[index], buildTree(l, index*2+1), buildTree(l, index*2+2))

def treeToList(root):
    l = [root]
    result = []
    while(l):
        node = l.pop(0)
        result.append(node.val)
        if(node.left):
            l.append(node.left)
        if(node.right):
            l.append(node.right)
    return result

def treesAreEqual(l, r):
    if l == None and r == None:
        return True
    if l == None or r == None:
        return False
    if l.val != r.val:
        return False
    return treesAreEqual(l.left, r.left) and treesAreEqual(l.right, r.right)
