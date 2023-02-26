import heapq
import math

class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        q = []
        min_val = math.inf
        for n in nums:
            if n%2:
                n *= 2
            min_val = min(min_val, n)
            heapq.heappush(q, 0-n)

        min_deviation = math.inf
        while q:
            n = 0 - heapq.heappop(q)
            min_deviation = min(min_deviation, abs(n - min_val))
            if n % 2:
                break
            n //= 2
            min_val = min(min_val, n)

            heapq.heappush(q, 0 - n)
        return min_deviation
            
