import heapq

class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:

        q = [(r2-r1, i) for i,(r1,r2) in enumerate(zip(reward1, reward2))]
        heapq.heapify(q)
        r1Indexes = set()
        for _ in range(k):
            diff, index = heapq.heappop(q)
            r1Indexes.add(index)

        result = 0
        for i,(r1,r2) in enumerate(zip(reward1, reward2)):
            result += r1 if i in r1Indexes else r2
        return result
