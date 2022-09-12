import math
from telnetlib import SE

class SegmentLeafNode:
    def __init__(self, slot):
        self.slot = slot
        self.value = 0

    def max_value(self, start, end_exclusive):
        if start <= self.slot < end_exclusive:
            return self.value
        else:
            return 0

    def set(self, slot, value):
        if self.slot != slot:
            raise Exception("Wrong slot, dumbass")
        self.value = value
        return self.value

class SegmentTreeNode:

    def get_child_node_ranges(self):
        midPoint = (self.range_end_exclusive +self.range_start) // 2
        return (self.range_start, midPoint), (midPoint, self.range_end_exclusive)

    def create_node(self, range_start, range_end_exclusive):
        if (range_end_exclusive - range_start) == 1:
            return SegmentLeafNode(range_start)
        else:
            return SegmentTreeNode(range_start, range_end_exclusive)

    def __init__(self, range_start, range_end_exclusive):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive
        self.cached_max = 0
        self.left = None
        self.right = None

    def max_value(self, start, end_exclusive):
        if self.range_end_exclusive <= start:
            return 0
        elif self.range_start >= end_exclusive:
            return 0
        elif self.range_start >= start and self.range_end_exclusive <= end_exclusive:
            return self.cached_max
        else:

            return max(
                self.left.max_value(start, end_exclusive) if self.left else 0,
                self.right.max_value(start, end_exclusive) if self.right else 0
            )

    def getOrCreateChildNode(self, slot):
        (left_start, left_end_exclusive), (right_start, right_end_exclusive) = self.get_child_node_ranges()
        if left_start <= slot < left_end_exclusive:
            if not self.left:
                self.left = self.create_node(left_start, left_end_exclusive)
            return self.left
        else:
            if not self.right:
                self.right = self.create_node(right_start, right_end_exclusive)
            return self.right

    def set(self, slot, value):
        node = self.getOrCreateChildNode(slot)
        child_max = node.set(slot, value)
        self.cached_max = max(child_max, self.cached_max)
        return self.cached_max

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        if not nums:
            return 0
        rootNode = SegmentTreeNode(0, 100001)
        max_value = 0
        l = []
        for n in nums:
            max_smaller = rootNode.max_value(n-k, n)
            current_value = rootNode.max_value(n, n+1)
            if current_value < max_smaller + 1:
                max_value = rootNode.set(n, max_smaller + 1)
        return max_value