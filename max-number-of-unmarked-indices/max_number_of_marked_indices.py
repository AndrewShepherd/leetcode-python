import heapq

class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums)
        left_half = nums[0:l//2]
        right_half = nums[l//2:]
        heapq.heapify(right_half)
        c = 0
        for n in left_half:
            if not right_half:
                break
            while(right_half):
                n2 = heapq.heappop(right_half)
                if n2 >= n*2:
                    c += 2
                    break
        return c