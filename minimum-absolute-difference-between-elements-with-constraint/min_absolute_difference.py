class TreeNode:
    def __init__(self, range_start, range_end_exclusive):
        self.left = None
        self.right = None
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive
        self.value = None

    def split(self):
        split_point = (self.range_start + self.range_end_exclusive)//2
        self.left = TreeNode(self.range_start, split_point)
        self.right = TreeNode(split_point, self.range_end_exclusive)
        if self.value != None and self.value < split_point:
            self.left.add(self.value)
        else:
            self.right.add(self.value)
        self.value = None
    
    def add(self, value):
        if self.value == value:
            return
        
        elif not(self.left and self.right) and self.value == None:
            self.value = value
            return
        elif not(self.left and self.right):
            self.split()
    
        if value < self.left.range_end_exclusive:
            self.left.add(value)
        else:
            self.right.add(value)

    def get_closest_value(self, target):
        if self.value != None:
            return self.value
        if (self.left == None):
            return None
        if target < self.range_start:
            v1 = self.left.get_closest_value(target)
            if v1 != None:
                return v1
            else:
                return self.right.get_closest_value(target)
        elif target >= self.range_end_exclusive:
            v1 = self.right.get_closest_value(target)
            if v1 != None:
                return v1
            else:
                return self.left.get_closest_value(target)
        else:
            v1 = self.left.get_closest_value(target)
            v2 = self.right.get_closest_value(target)
            if v1 == None:
                return v2
            elif v2 == None:
                return v1
            else:
                return v1 if abs(target - v1) < abs(target - v2) else v2  
    

class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        min_nums = min(nums)
        max_nums = max(nums)
        tree = TreeNode(min_nums, max_nums + 1)
        best_result = 1000000001
        for i in range(x, len(nums)):
            n = nums[i]
            tree.add(nums[i - x])
            closest = tree.get_closest_value(n)
            best_result = min(best_result, abs(n - closest))
        return best_result
    
        
