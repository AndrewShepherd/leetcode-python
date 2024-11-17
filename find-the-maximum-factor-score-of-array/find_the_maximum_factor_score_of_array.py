def gcd(l, r):
    l,r = min(l, r), max(l, r)
    if r%l == 0:
        return l
    else:
        return gcd(l, r%l)


def calculateMaxScore(nums: list[int]) -> int:
    d = nums[0]
    m = nums[0]
    for i in range(1, len(nums)):
        next_d = gcd(d, nums[i])
        d = next_d
    m = 1
    for n in nums:
        m = m * n // gcd(m,n)
    return d * m

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0] * nums[0]
        
        result = calculateMaxScore(nums)
        for i in range(len(nums)):
            result = max(result, calculateMaxScore(nums[:i] + nums[i+1:]))

        return result
