import heapq

class Solution:
    def fillCups(self, amount) -> int:
        q = []
        for a in amount:
            if a > 0:
                heapq.heappush(q, 0-a)
        t = 0
        while q:
            if len(q) == 1:
                return t - q[0]
            c1 = 0 - heapq.heappop(q)
            c2 = 0 - heapq.heappop(q)
            t += 1
            c1 -= 1
            c2 -= 1
            if c1:
                heapq.heappush(q, 0 - c1)
            if c2:
                heapq.heappush(q, 0 - c2)
        return t