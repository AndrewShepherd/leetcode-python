class EmptyNode:

    def __len__(self):
        return 0
    
    def block(self, start, end_exclusive):
        return self

EMPTY = EmptyNode()

def create_node(range_start, range_end_exclusive, left_node, right_node):
    new_length = len(left_node) + len(right_node)
    if new_length == 0:
        return EMPTY
    elif len(left_node) == 0:
        return right_node
    elif len(right_node) == 0:
        return left_node
    else:
        return BranchNode(range_start, range_end_exclusive, left_node, right_node)


class CompleteNode:
    def __init__(self, start, end_exclusive):
        self.start = start
        self.end_exclusive = end_exclusive

    def __len__(self):
        return self.end_exclusive - self.start
    
    def block(self, start, end_exclusive):
        if start >= self.end_exclusive:
            return self
        if end_exclusive <= self.start:
            return self
        if self.start >= start and self.end_exclusive <= end_exclusive:
            return EMPTY
        mid_point = (self.start + self.end_exclusive) // 2        
        new_left_child = CompleteNode(self.start, mid_point).block(start, end_exclusive)
        new_right_child = CompleteNode(mid_point, self.end_exclusive).block(start, end_exclusive)
        return create_node(self.start, self.end_exclusive, new_left_child, new_right_child)

    
class BranchNode:

    def __init__(self, start, end_exclusive, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child
        self.length = len(left_child) + len(right_child)
        self.start = start
        self.end_exclusive = end_exclusive

    def block(self, start, end_exclusive):
        if start >= self.end_exclusive:
            return self
        if end_exclusive <= self.start:
            return self
        if self.start >= start and self.end_exclusive <= end_exclusive:
            return EMPTY
        new_left_child = self.left_child.block(start, end_exclusive)
        new_right_child = self.right_child.block(start, end_exclusive)
        return create_node(self.start, self.end_exclusive, new_left_child, new_right_child)
        
    def __len__(self):
        return self.length

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        node = CompleteNode(0, n)
        result = [None] * len(queries)
        for i, (start, end) in enumerate(queries):
            node = node.block(start + 1, end)
            result[i] = len(node) -1
        return result
