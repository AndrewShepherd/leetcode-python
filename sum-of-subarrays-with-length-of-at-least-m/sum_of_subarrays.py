from math import inf

class Solution:
    def maxSum(self, nums: list[int], k: int, m: int) -> int:
        # Find the longest sub array of at least m

        best = [None] * len(nums)
        for segment_index in range(k):
            segment_start = segment_index * m
            at_least = [None] * m
            best2 = [None] * len(nums)
            for i in range(segment_start, len(nums)):
                n = nums[i]
                at_least2 = [None] * m
                for i2, n2 in enumerate(at_least):
                    if i2 == 0:
                        best_before = None
                        if (i > 0):
                            best_before = best[i-1]
                        if best_before == None:
                            best_before = 0
                        just_this_one = n + best_before
                        if n2 == None:
                            at_least2[i2] = just_this_one
                        else:
                            # This is where the logical error is
                            at_least2[i2] = max(just_this_one, just_this_one + n2)
                    else:
                        if at_least[i2 - 1] != None:
                            at_least2[i2] = at_least[i2 - 1] + n
                at_least = at_least2
                if (at_least[-1] != None):
                    before = -inf if (i == 0 or best2[i-1] == None) else best2[i-1]
                    best2[i] = max(before, at_least[-1])
            best = best2
        return best[-1]
