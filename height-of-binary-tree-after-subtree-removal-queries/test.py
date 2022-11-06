import unittest


from tree_queries import Solution, create_node_lookup

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
        root = buildTree([1,3,4,2,null,6,5,null,null,null,null,null,7])
        
        nl = create_node_lookup(root)
        n = nl[4]
        self.assertEqual(2, n.height)
        s = Solution()
        result = s.treeQueries(root, [4])
        expectedResult = [2]
        self.assertEqual(expectedResult, result)

    def test_2(self):
        root = buildTree([5,8,9,2,1,3,7,4,6])
        s = Solution()
        result = s.treeQueries(root, [3,2,4,8])
        expectedResult = [3,2,3,2]
        self.assertEqual(expectedResult, result)


try:
    unittest.main()
except SystemExit:
    None



