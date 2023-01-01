# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def iterate_through_list(head):
    while(head):
        yield head.val
        head = head.next

class Solution:
    def removeNodes(self, head):
        asList = list(iterate_through_list(head))
        maxSoFar = 0
        for i in range(len(asList)-1, -1, -1):
            maxSoFar = max(maxSoFar, asList[i])
            asList[i] = maxSoFar
        
        first_item_kept = None
        item_to_append_to = None
        i = 0
        while head and i < len(asList):
            if head.val >= asList[i]:
                if (first_item_kept == None):
                    first_item_kept = head
                    item_to_append_to = head
                else:
                    item_to_append_to.next = head
                    item_to_append_to = head
            head = head.next
            i += 1
        return first_item_kept
