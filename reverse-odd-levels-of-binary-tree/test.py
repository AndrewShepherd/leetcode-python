import unittest


from reverse_odd_levels_of_binary_tree import Solution

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
        root = buildTree([2,3,5,8,13,21,34])
        
        s = Solution()
        result = s.reverseOddLevels(root)
        expectedResult = buildTree([2,5,3,8,13,21,34])
        self.assertEqual(treeToList(result), treeToList(expectedResult))

    def test_2(self):
        root = buildTree([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
        s = Solution()
        result = s.reverseOddLevels(root)
        expectedResult = buildTree([0,2,1,0,0,0,0,2,2,2,2,1,1,1,1])
        self.assertEqual(treeToList(result), treeToList(expectedResult))


try:
    unittest.main()
except SystemExit:
    None


