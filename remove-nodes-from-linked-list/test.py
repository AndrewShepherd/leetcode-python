import unittest
from remove_nodes_from_linked_list import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(l):
    head = None
    for v in reversed(l):
        head = ListNode(v, head)
    return head

def iterate_through_list(head):
    while(head):
        yield head.val
        head = head.next


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        l = build_list([5,2,13,3,8])
        result = s.removeNodes(l)
        resultList = list(iterate_through_list(result))
        self.assertEqual([13,8], resultList)


try:
    unittest.main()
except SystemExit:
    None

