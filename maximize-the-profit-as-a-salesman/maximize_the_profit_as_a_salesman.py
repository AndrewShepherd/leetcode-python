import bisect

class RangeTreeNode:

    def __init__(self, range_start, range_end_exclusive):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive
        self.index = None
        self.value = None
        self.left = None
        self.right = None

    def is_empty(self):
        return self.left == None and self.value == None

    def split(self):
        split_point = (self.range_end_exclusive + self.range_start)//2
        self.left = RangeTreeNode(self.range_start, split_point)
        self.right = RangeTreeNode(split_point, self.range_end_exclusive)
        existing_value = self.value
        existing_index = self.index
        self.value = None
        self.index = None
        self.add(existing_index, existing_value)

    def get_all_values(self):
        if self.value != None:
            return [(self.index, self.value)]
        elif self.left == None:
            return []
        else:
            result = []
            result.extend(self.left.get_all_values())
            result.extend(self.right.get_all_values())
            return result
        
    def prune(self, less_or_equal_to: int):
        if self.is_empty():
            return
        elif self.value != None:
            if self.value <= less_or_equal_to:
                self.index = None
                self.value = None
        else:
            self.left.prune(less_or_equal_to)
            self.right.prune(less_or_equal_to)
            if self.left.is_empty() and self.right.is_empty():
                self.left = None
                self.right = None

    def add(self, index, value):

        if self.is_empty():
            self.index = index
            self.value = value
            return
        elif self.index == index:
            self.value = max(value, self.value)
            return
        elif self.left == None:
            self.split()
        if index <= self.left.range_end_exclusive:
            self.left.add(index, value)
            ## Right could hold more than one value
            # Must make it prune all values <= value
            self.right.prune(value)
        else:
            self.right.add(index, value)
        
    def get_best_value_up_to(self, index):
        if self.is_empty():
            return None
        elif self.index != None:
            return self.value if self.index <= index else None
        else:
            if self.right.range_start <= index:
                right_value = self.right.get_best_value_up_to(index)
                if right_value != None:
                    return right_value
            return self.left.get_best_value_up_to(index)

        
    def max_value(self):
        if self.value != None:
            return self.value
        elif self.left == None:
            return None
        else:
            left_value = self.left.max_value()
            right_value = self.right.max_value()
            valid_values = [v for v in [left_value, right_value] if v != None]
            if not valid_values:
                return None
            return max(valid_values)

class Solution:
    def maximizeTheProfit(self, n: int, offers: list[list[int]]) -> int:
        offers.sort()
        root_node = RangeTreeNode(0, n + 1)
        root_node.add(0, 0)

        for i, (start, end_inclusive, price) in enumerate(offers):
            v = root_node.get_best_value_up_to(start) + price
            competitor = root_node.get_best_value_up_to(end_inclusive+1)
            if v > competitor:
                root_node.add(end_inclusive + 1, v)
        return root_node.max_value()
