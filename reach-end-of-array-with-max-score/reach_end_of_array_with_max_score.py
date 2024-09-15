class Solution:
    # def findMaximumScore(self, nums: list[int]) -> int:
    #     result = [None] * len(nums)
    #     result[0] = 0
    #     for i in range(1, len(nums)):
    #         result[i] = max( [result[j] + nums[j] * (i-j) for j in range(i)])
    #     return result[-1]
    def findMaximumScore(self, nums: list[int]) -> int:
        result = 0
        last_number = 0
        for n in nums:
            result += last_number
            last_number = max(last_number, n)
        return result

