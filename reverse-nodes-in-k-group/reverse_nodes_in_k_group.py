# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseK(head: ListNode, k):
    first = head
    for _ in range(k-1):
        nodeToMoveToFront = head.next
        head.next = nodeToMoveToFront.next
        nodeToMoveToFront.next = first
        first = nodeToMoveToFront
    return first, head
        
def countList(head: ListNode):
    c = 0
    n = head
    while(n):
        c += 1
        n = n.next
    return c

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head

        c = countList(head)
        if c < k:
            return head
        head, last = reverseK(head, k)
        for _ in range(k, c-k+1, k):
            last.next, last = reverseK(last.next, k)
        return head