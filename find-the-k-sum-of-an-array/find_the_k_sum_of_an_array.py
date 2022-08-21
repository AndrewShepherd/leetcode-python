import heapq

class Solution:
    def kSum(self, nums, k: int) -> int:
        diffs = [abs(n) for n in nums]
        sumPositives = sum(n for n in nums if n > 0)
        diffs.sort()

        q = []

        for n in range(2**len(nums)):
            index=0
            mask=1
            t = 0
            while n >= mask:
                if n & mask:
                    t += diffs[index]
                mask = mask << 1
                index += 1
            if len(q) == k:
                other = heapq.heappop(q)
                heapq.heappush(q, max(other, 0-t))
            else:
                heapq.heappush(q, 0-t)
        return sumPositives + q[0]
