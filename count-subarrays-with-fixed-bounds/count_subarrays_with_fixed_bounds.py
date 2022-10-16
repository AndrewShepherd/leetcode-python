from functools import cache

class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:

        pending_min_starts = 0
        pending_max_starts = 0
        min_constraint_fulfilled = False
        max_constraint_fulfilled = False
        possible_starts = 0
        count = 0
        for i,n in enumerate(nums):
            if n < minK or n > maxK:
                pending_min_starts = 0
                pending_max_starts = 0
                min_constraint_fulfilled = False
                max_constraint_fulfilled = False
                possible_starts = 0
            if n == minK and n == maxK:
                possible_starts += 1
            elif n == minK:
                min_constraint_fulfilled = True
                if max_constraint_fulfilled:
                    possible_starts += pending_max_starts
                    pending_max_starts = 0
                else:
                    pending_min_starts += 1
            elif n == maxK:
                max_constraint_fulfilled = True
                if min_constraint_fulfilled:
                    possible_starts += pending_min_starts
                    pending_min_starts = 0
                else:
                    pending_max_starts += 1
            count += possible_starts
        return count
