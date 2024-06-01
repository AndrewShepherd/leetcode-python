from collections import Counter

    
    
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums1 = [n // k for n in nums1 if n % k == 0]
        if len(nums1) == 0:
            return 0
        c = Counter(nums2)
        s = [0] * (max(nums1) + 1)
        for value, count in c.items():
            for i in range(value, len(s), value):
                s[i] += count

        return sum(s[n] for n in nums1)


