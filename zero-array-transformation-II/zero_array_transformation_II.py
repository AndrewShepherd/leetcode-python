def create_node(range_start, range_end_exclusive, index, value):
    if range_end_exclusive - range_start == 1:
        if value == 0:
            return EmptyNode()
        else:
            return ValueNode(value)
    else:
        return BranchNode(range_start, range_end_exclusive, None, None).set_value(index, value)

class InitialNode:
    def __init__(self, count):
        self.count = count

    def set_value(self, index, value):
        return BranchNode(0, self.count, None, None).set_value(index, value)
    
class BranchNode:
    def __init__(self, range_start, range_end_exclusive, left_node, right_node, subtract_amount = 0):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive
        self.left_node = left_node
        self.right_node = right_node
        self.subtract_amount = subtract_amount
        max_child_value = max(0 if self.left_node == None else self.left_node.max_value, 0 if self.right_node == None else self.right_node.max_value)
        self.max_value = max_child_value - subtract_amount

    def subtract(self, range_start, range_end_exclusive, value):
        if range_start <= self.range_start and range_end_exclusive >= self.range_end_exclusive:
            if value >= self.max_value:
                return EmptyNode()
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
            max_child_value = max(0 if left_node == None else left_node.max_value, 0 if right_node == None else right_node.max_value)
            if max_child_value - self.subtract_amount <= 0:
                return EmptyNode()
            else:
                return BranchNode(self.range_start, self.range_end_exclusive, left_node, right_node, self.subtract_amount)

    def set_value(self, index, value):
        mid_point = (self.range_start + self.range_end_exclusive) // 2
        left_node = self.left_node
        right_node = self.right_node
        if index < mid_point:
            if self.left_node == None:
                left_node = create_node(self.range_start, mid_point, index,value)
            else:
                left_node = self.left_node.set_value(index, value)
        else:
            if self.right_node == None:
                right_node = create_node(mid_point, self.range_end_exclusive, index, value)
            else:
                right_node = self.right_node.set_value(index, value)
        return BranchNode(self.range_start, self.range_end_exclusive, left_node, right_node, self.subtract_amount)
    
class ValueNode:
    def __init__(self, value):
        self.max_value = value

    def subtract(self, range_start, range_end_exclusive, value):
        if value >= self.max_value:
            return EmptyNode()
        else:
            return ValueNode(self.max_value - value)

class EmptyNode:
    def __init__(self):
        self.max_value = 0
    def subtract(self, range_start, range_end_exclusive, value):
        return self


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        if all([n == 0 for n in nums]):
            return 0
        node = InitialNode(len(nums))
        for i,n in enumerate(nums):
            node = node.set_value(i, n)
        for i,(range_start, range_end, value) in enumerate(queries):
            node = node.subtract(range_start, range_end + 1, value)
            if node.max_value == 0:
                return i+1
        return -1
