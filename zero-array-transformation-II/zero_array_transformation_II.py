class EmptyNode:
    def __init__(self):
        self.max_value = 0
    def subtract(self, range_start, range_end_exclusive, value):
        return self
    
EMPTY = EmptyNode()
    
class BranchNode:
    def __init__(self, range_start, range_end_exclusive, left_node, right_node, subtract_amount = 0):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive
        self.left_node = left_node
        self.right_node = right_node
        self.subtract_amount = subtract_amount
        max_child_value = max(self.left_node.max_value, self.right_node.max_value)
        self.max_value = max_child_value - subtract_amount

    def subtract(self, range_start, range_end_exclusive, value):
        if range_start <= self.range_start and range_end_exclusive >= self.range_end_exclusive:
            if value >= self.max_value:
                return EMPTY
            else:
                return BranchNode(self.range_start, self.range_end_exclusive, self.left_node, self.right_node, self.subtract_amount + value)
        else:
            mid_point = (self.range_start + self.range_end_exclusive) // 2
            left_node = self.left_node
            right_node = self.right_node
            if range_start < mid_point:
                left_node = left_node.subtract(range_start, min(mid_point, range_end_exclusive), value)
            if range_end_exclusive > mid_point:
                right_node = right_node.subtract(max(mid_point, range_start), range_end_exclusive, value)
            max_child_value = max(left_node.max_value, right_node.max_value)
            if max_child_value - self.subtract_amount <= 0:
                return EMPTY
            else:
                return BranchNode(self.range_start, self.range_end_exclusive, left_node, right_node, self.subtract_amount)

class ValueNode:
    def __init__(self, value):
        self.max_value = value

    def subtract(self, range_start, range_end_exclusive, value):
        if value >= self.max_value:
            return EMPTY
        else:
            return ValueNode(self.max_value - value)


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        # Build the tree
        nodes = [ValueNode(n) for i,n in enumerate(nums)]
        m = 1
        while(len(nodes) > 1):
            nodes2 = []
            m *= 2
            for i in range(0, len(nodes), 2):
                left_node = nodes[i]
                right_node = nodes[i+1] if i+1 < len(nodes) else EMPTY
                range_start = len(nodes2) * m
                range_end = (len(nodes2) + 1) * m
                nodes2.append(BranchNode(range_start, range_end, left_node, right_node, 0))
            nodes = nodes2

        node = nodes[0]

        if node.max_value == 0:
            return 0

        for i,(range_start, range_end, value) in enumerate(queries):
            node = node.subtract(range_start, range_end + 1, value)
            if node.max_value == 0:
                return i+1
        return -1
