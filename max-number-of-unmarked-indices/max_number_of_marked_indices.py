import bisect

class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        print(f"{nums}")
        marked = [False] * len(nums)
        left_top = len(nums)

        count = 0
        for i in range(len(nums)-1, -1, -1):
            if marked[i]:
                continue
            r = nums[i]
            lIndex = bisect.bisect_right(nums, r//2, 0, left_top)
            while(lIndex >= 0):
                if not marked[lIndex] and (nums[lIndex] <= r//2):
                    marked[lIndex] = True
                    marked[i] = True # unnecessary
                    count += 2
                    left_top = lIndex
                    print(f"{nums[lIndex]} - {nums[i]}")
                    break
                lIndex -= 1

        remaining = [nums[i] for i in range(len(nums)) if not marked[i]]
        return count
