from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # Find k
        for kIndex, v in enumerate(nums):
            if v == k:
                break
        dLeft = defaultdict(lambda: 0)
        lessThanK = 0
        greaterThanK = 0
        for i in range(kIndex-1, -1, -1):
            v = nums[i]
            if v < k:
                lessThanK += 1
            else:
                greaterThanK += 1
            dLeft[greaterThanK - lessThanK] += 1

        dRight = defaultdict(lambda: 0)
        lessThanK = 0
        greaterThanK = 0
        for i in range(kIndex + 1, len(nums)):
            v = nums[i]
            if v < k:
                lessThanK += 1
            else:
                greaterThanK += 1
            dRight[greaterThanK - lessThanK] += 1

        total = 1 + dLeft[0] + dRight[0] + dLeft[1] + dRight[1]
        for k,v in dLeft.items():
            total += v * dRight[0-k]
            total += v * dRight[0-k+1]

        return total
