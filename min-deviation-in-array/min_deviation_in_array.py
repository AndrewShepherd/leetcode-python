class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        nums = set(nums)
        lower = min(nums)
        higher = max(nums)
        prev_min_maxes = set()
        while(True):
            if lower == higher:
                return 0
            if (lower,higher) in prev_min_maxes:
                print(f"{(lower,higher)} in {prev_min_maxes}")
                return higher - lower
            prev_min_maxes.add((lower,higher))
            print(f"nums = {sorted(nums)}")

            nums.remove(lower)
            nums.remove(higher)
            diff_before = higher - lower
            if higher % 2 == 0:
                higher //= 2
            elif lower % 2 == 1:
                lower *= 2
            else:
                return diff_before
            if abs(higher - lower) >= diff_before:
                return diff_before
            nums.add(higher)
            nums.add(lower)
            lower = min(nums)
            higher = max(nums)
 #           diff_after = higher - lower
 #           if diff_after >= diff_before:
 #               return diff_before

