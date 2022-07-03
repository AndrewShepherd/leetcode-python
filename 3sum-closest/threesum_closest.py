import math

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        nums.sort()
        best_value = math.inf
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                this_sum = nums[i] + nums[j] + nums[k]
                diff = abs(target - this_sum)
                if diff < abs(target - best_value):
                    best_value = this_sum
                    if diff == 0:
                        return best_value
                if this_sum < target:
                    j += 1
                else:
                    k -= 1
        return best_value
