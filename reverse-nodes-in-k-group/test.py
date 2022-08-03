import unittest
from reverse_nodes_in_k_group import Solution, ListNode, reverseK



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


    def test_reverse2(self):
        s = Solution()
        l = makeLinkedList([1,2,3,4,5])
        first, last = reverseK(l, 2)
        self.assertEqual(first.val, 2)
        self.assertEqual(last.val, 1)
        result = s.reverseKGroup(makeLinkedList([1,2,3,4,5]), 2)
        
    def test_reverse3(self):
        s = Solution()
        l = makeLinkedList([1,2,3,4,5])
        first, last = reverseK(l, 3)
        self.assertEqual(first.val, 3)
        self.assertEqual(first.next.val, 2)
        self.assertEqual(first.next.next.val, 1)
        self.assertEqual(last.val, 1)
        self.assertEqual(last.next.val, 4)
        result = s.reverseKGroup(makeLinkedList([1,2,3,4,5]), 2)

try:
    unittest.main()
except SystemExit:
    None