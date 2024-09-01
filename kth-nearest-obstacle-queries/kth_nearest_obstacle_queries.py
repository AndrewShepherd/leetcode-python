import heapq

class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        q = []
        result = []
        distances = [abs(x) + abs(y) for x,y in queries]
        for d in distances:
            if len(q) < k:
                heapq.heappush(q, 0-d)
            else:
                if (d < abs(q[0])):
                    heapq.heappushpop(q, 0-d)
            result.append(-1 if len(q) < k else 0-q[0])
        return result
                
                    
