import heapq

class Solution:
    def minGroups(self, intervals) -> int:
        if not intervals:
            return 0
        heap = []
        max_length = 0
        intervals.sort()
        for r in [intervals[i] for i in range(0, len(intervals))]:
            while heap and r[0] > heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, r[1])
            max_length = max(max_length, len(heap))
        return max_length
