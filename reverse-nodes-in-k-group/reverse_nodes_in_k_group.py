# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##################
#
#  

def reverseK(head: ListNode, k):
    newHead = head.next
    head.next = newHead.next
    newHead.next = head

    first = newHead
    for _ in range(k-2):
        nodeToMoveToFront = head.next
        newLast = nodeToMoveToFront.next
        head.next = newLast
        nodeToMoveToFront.next = first
        first = nodeToMoveToFront

    return first, head
        
    

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        # first count them
        c = 0
        n = head
        while(n):
            c += 1
            n = n.next
        if c < k:
            return head
        head, last = reverseK(head, k)
        _ = k
        while _+k < c+1:
            last.next, last = reverseK(last.next, k)
            _ += k
        return head