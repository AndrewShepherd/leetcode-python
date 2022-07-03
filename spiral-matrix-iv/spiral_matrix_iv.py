# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def iterateThroughNodes(head):
    while head:
        yield head.val
        head = head.next

def getSpiralIndexes(m, n):
    # m = height
    # n = width
    x_min = 0
    x_max_exclusive = n
    y_min = 0
    y_max_exclusive = m
    while x_min < x_max_exclusive and y_min < y_max_exclusive:
        y = y_min
        for x in range(x_min, x_max_exclusive):
            yield (x, y)
        y_min += 1
        for y in range(y_min, y_max_exclusive):
            yield(x, y)
        x_max_exclusive -= 1
        for x in range(x_max_exclusive - 1, x_min - 1, -1):
            yield(x, y)
        y_max_exclusive -= 1
        for y in range(y_max_exclusive - 1, y_min - 1, -1):
            yield(x, y)
        x_min += 1

class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        matrix = [None] * m
        for i in range(m):
            matrix[i] = [-1] * n
        for v, (column, row) in zip(iterateThroughNodes(head), getSpiralIndexes(m, n)):
            matrix[row][column] = v
        return matrix