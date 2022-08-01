class TreeNode:
    def __init__(self, nums, start: int, endExclusive: int):
        self.index = (start + endExclusive)//2
        self.start = start
        self.endExclusive = endExclusive
        self.value = nums[self.index]
        self.sum = self.value
        if self.index > self.start:
            self.left = TreeNode(nums, start, self.index)
            self.sum += self.left.sum
        if self.index + 1 < endExclusive:
            self.right = TreeNode(nums, self.index+1, endExclusive)
            self.sum += self.right.sum
            
    def update(self, index:int, val:int) -> int:
        if index == self.index:
            diff = val - self.value
            self.value = val
        elif index < self.index:
            diff = self.left.update(index, val)
        else:
            diff = self.right.update(index, val)
        self.sum += diff
        return diff
    
    def sumRange(self, left, right) -> int:
        if left > self.index:
            return self.right.sumRange(left, right)
        elif right < self.index:
            return self.left.sumRange(left, right)
        else:
            result = self.sum
            if left > self.start:
                result -= self.left.sumRange(self.start, left-1)
            if right < self.endExclusive-1:
                result -= self.right.sumRange(right+1, self.endExclusive-1 )
            return result


class NumArray:

    def __init__(self, nums: list):
        self.nums = nums
        self.tree = TreeNode(nums, 0, len(nums))

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sumRange(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)