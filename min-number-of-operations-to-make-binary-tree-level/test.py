import unittest

from minimum_operations import Solution

null = None

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



class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        tree = buildTree([1,4,3,7,6,8,5,null,null,null,null,9,null,10])
        result = s.minimumOperations(tree)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        tree = buildTree([1,3,2,7,6,5,4])
        result = s.minimumOperations(tree)
        self.assertEqual(3, result)

    def test_3(self):
        s = Solution()
        tree = buildTree([1,2,3,4,5,6])
        result = s.minimumOperations(tree)
        self.assertEqual(0, result)

    def test_0(self):
        tree_input = [332,463,103,417,150,409,41,135,129,117,474,263,null,328,456,347,167,383,null,null,422,493,489,275,72,null,null,425,89,null,null,162,18,null,null,null,null,363,290,106,260,468,null,null,null,432,null,323,null,null,null,null,null,null,36,null,null,302,190,null,280,null,null,null,null,488,null,null,null,null,446,null,null,null,null,null,75]
        tree = buildTree(tree_input)
        s = Solution()
        result = s.minimumOperations(tree)
        self.assertEqual(24, result)
try:
    unittest.main()
except SystemExit:
    None






