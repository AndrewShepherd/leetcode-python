class MyFunkyDataStructure:

    def __init__(self):
        self.l = [(-100001, 0)]

    def get(self, less_than_or_equal_to):
        for i in range(len(self.l)-1, -1, -1):
            y_intercept, value = self.l[i]
            if y_intercept <= less_than_or_equal_to:
                return value
    
    def set(self, y_intercept, value):
        other_list = []
        while(self.l[-1][0] >= y_intercept):
            other_list.append(self.l.pop())
        y2, v2, = self.l[-1]
        if value > v2:
            if y2 == y_intercept:
                self.l[-1] = (y_intercept, value)
            else:
                self.l.append((y_intercept, value))
        while(other_list):
            y2, v2 = other_list.pop()
            if v2 > self.l[-1][1]:
                self.l.append((y2,v2))
        


class Solution:
    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
        
        indexes_and_nums = [(i,n) for i,n in enumerate(nums) if n > 0]
        if len(indexes_and_nums) <= 1:
            return max(nums)

        b = MyFunkyDataStructure()
        for index in range(0, len(indexes_and_nums)):
            i, n = indexes_and_nums[index]
            this_y_intercept = n - i
            v = b.get(this_y_intercept)
            b.set(this_y_intercept, v + n)

        return b.l[-1][1]