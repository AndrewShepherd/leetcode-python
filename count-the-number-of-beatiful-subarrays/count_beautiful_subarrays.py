from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        d = defaultdict(lambda:0)
        d[0] = 1
        count = 0
        aggregate = 0
        for n in nums:
            aggregate ^= n
            if d[aggregate]:
                count += d[aggregate]
            d[aggregate] += 1
        return count
