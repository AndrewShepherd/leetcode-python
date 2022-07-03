import unittest
from spiral_matrix_iv import Solution, ListNode



def makeLinkedList(input):
    if not input:
        return None
    head = ListNode(input[0])
    cursor = head
    for n in input[1:]:
        newNode = ListNode(n)
        cursor.next = newNode
        cursor = newNode
    return head

class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.spiralMatrix(3, 5, makeLinkedList([3,0,2,6,8,1,7,9,4,2,5,5,0]))
        self.assertEqual(result, [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]])

    def test_1(self):
        s = Solution()
        result = s.spiralMatrix(1, 4, makeLinkedList([0,1,2]))
        self.assertEqual(result, [[0,1,2,-1]])

try:
    unittest.main()
except SystemExit:
    None