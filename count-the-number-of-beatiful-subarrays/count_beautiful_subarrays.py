from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        beautiful_count = 0
        previous = defaultdict(lambda:0)
        for n in nums:
            new_dict = defaultdict(lambda:0)
            new_dict[n] = 1
            for k,v in previous.items():
                new_key = n ^ k
                new_dict[new_key] += v
            beautiful_count += new_dict[0]
            previous = new_dict
        return beautiful_count
