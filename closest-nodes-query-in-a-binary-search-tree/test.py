import unittest

from closest_nodes import Solution

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

null = None


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        tree = buildTree([6,2,13,1,4,9,15,null,null,null,null,null,null,14])
        result = s.closestNodes(tree, [2, 5, 16])
        self.assertEqual([[2,2],[4,6],[15,-1]], result)

    def test_0(self):
        s = Solution()
        tree = buildTree([6,2,13,1,4,9,15,null,null,null,null,null,null,14])
        result = s.closestNodes(tree, [16, 2, 5])
        self.assertEqual([[15,-1],[2,2],[4,6]], result)

    def test_2(self):
        s = Solution()
        tree = buildTree([4,null,9])
        result = s.closestNodes(tree, [3])
        self.assertEqual([[-1, 4]], result)


try:
    unittest.main()
except SystemExit:
    None









