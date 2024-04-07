class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        nums.sort()
        total = 0
        
        if len(nums)%2:
            median_point = len(nums)//2
            for i,n in enumerate(nums):
                if i < median_point:
                    if n > k:
                        total += n-k
                elif i > median_point:
                    if n < k:
                        total += k-n
                else:
                    total += abs(k-n) 
        else:
            median_point = len(nums)//2
            for i,n in enumerate(nums):
                if i < median_point:
                    if n > k:
                        total += n-k
                elif i > median_point:
                    if n < k:
                        total += k-n
                else:
                    total += abs(k-n) 
            # larger_median = len(nums)//2
            # smaller_median = larger_median - 1
            # for i,n in enumerate(nums):
            #     if i < smaller_median:
            #         if n > k:
            #             total += n-k
            #     elif i > larger_median:
            #         if n < k:
            #             total += k-n
            #     total += abs(2 * k - (nums[smaller_median] + nums[larger_median]))

        return total
