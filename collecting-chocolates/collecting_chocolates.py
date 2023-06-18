from collections import defaultdict
import heapq
import math



def calculate_sliding_value_mins(nums: list[int], window_size: int) -> int:
    if window_size == 1:
        return sum(nums)
    if window_size == len(nums):
        return min(nums) * len(nums)
    total = 0
    q = []
    d = defaultdict(int)
    for i in range(0, window_size):
        n = nums[i]
        if d[n] == 0:
            q.append(n)
        d[n] += 1
    heapq.heapify(q)
    index_first = 0
    index_last = window_size-1
    for _ in range(len(nums)):
        total += q[0]
        index_last = (index_last + 1) % len(nums)
        d[nums[index_last]] += 1
        if d[nums[index_last]] == 1:
            heapq.heappush(q, nums[index_last])
        d[nums[index_first]] -= 1
        while d[q[0]] == 0:
            heapq.heappop(q)
        index_first = (index_first + 1) % len(nums)
    return total


class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        best_result = math.inf
        for shifts in range(len(nums)):
            if shifts * x >= best_result:
                break
            best_result = min(
                best_result,
                calculate_sliding_value_mins(nums, shifts+1) + shifts * x
            )
        return best_result
