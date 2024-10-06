import heapq

class QueueEntry:
    def __init__(self, available_start, base_value, multiplier):
        self.base_value = base_value
        self.multiplier = multiplier
        self.end_time = available_start + self.base_value * self.multiplier

    
    def work(self):
        return QueueEntry(self.end_time, self.base_value, self.multiplier + 1)
    
    def __lt__(self, other):
        return self.end_time < other.end_time
    

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        q = [QueueEntry(0, w, 1) for w in workerTimes]
        heapq.heapify(q)
        seconds = 0
        for _ in range(mountainHeight):
            seconds = q[0].end_time
            heapq.heapreplace(q, q[0].work())
        return seconds
