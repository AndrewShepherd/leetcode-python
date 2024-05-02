from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        total_count = len(nums) * (len(nums) + 1)//2
        m = (total_count // 2 + 1) if total_count % 2 else (total_count // 2)        

        def subListsWithNoMoreThan(n):
            if n < 1:
                return 0
            window_start = 0
            window_end_exclusive = 0
            d = dict()
            t = 0
            while(window_end_exclusive < len(nums)):
                num = nums[window_end_exclusive]
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
                while(len(d.keys()) > n):
                    to_remove = nums[window_start]
                    if d[to_remove] == 1:
                        del d[to_remove]
                    else:
                        d[to_remove] -= 1
                    window_start += 1
                window_end_exclusive += 1
                l = window_end_exclusive - window_start
                t += l
            return t

        left = 1
        right = len(nums)
        while(right-left > 0):
            middle = (left + right)//2
            result = subListsWithNoMoreThan(middle)
            if result < m:
                left = middle + 1
            else:
                right = middle
        return right

