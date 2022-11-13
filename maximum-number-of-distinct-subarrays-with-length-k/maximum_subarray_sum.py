class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if k == 1:
            return max(nums)
        left = 0
        right = 0
        s = set([nums[0]])
        sum_s = nums[0]
        count = 0
        right += 1
        while(right < len(nums)):
            n = nums[right]
            while n in s:
                s.remove(nums[left])
                sum_s -= nums[left]
                left += 1
            s.add(n)
            sum_s += n
            if right-left+1 == k:
                count = max(count, sum_s)
                s.remove(nums[left])
                sum_s -= nums[left]
                left += 1
            right += 1
        return count
