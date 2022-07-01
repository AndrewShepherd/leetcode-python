import heapq

def scheduleCourse(A):
    pq = []
    start = 0
    for t, end in sorted(A, key = lambda c: c[1]):
        start += t
        heapq.heappush(pq, -t)
        while start > end:
            start += heapq.heappop(pq)
    return len(pq)