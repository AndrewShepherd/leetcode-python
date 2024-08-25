import heapq

MODULO = 10**9 + 7


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        q = [(n, i) for i,n in enumerate(nums)]
        heapq.heapify(q)
        for _ in range(k):
            n,i = heapq.heappop(q)
            heapq.heappush(q, (n*multiplier, i))
        
        result = [0] * len(nums)
        for n,i in q:
            result[i] = n % MODULO
        return result
