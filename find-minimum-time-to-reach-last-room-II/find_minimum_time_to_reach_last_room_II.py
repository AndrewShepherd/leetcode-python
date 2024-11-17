import heapq

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])

        def get_adjacencies(row, col):
            for dR, dC in deltas:
                row2 = row + dR
                col2 = col + dC
                if (0 <= row2 < rows) and (0 <= col2 < cols):
                    yield (row2, col2)

        visited = [[False] * cols for _ in range(rows)]

        q = []
        heapq.heappush(q, (0, 1, (0, 0)))
        while q:
            t, s, (row, col) = heapq.heappop(q)
            if visited[row][col]:
                continue
            if row == rows-1 and col == cols-1:
                return t
            visited[row][col] = True
            for adjRow, adjCol in get_adjacencies(row, col):
                if visited[adjRow][adjCol]:
                    continue
                t2 = max(t+s, moveTime[adjRow][adjCol]+s)
                heapq.heappush(q, (t2, 2 if s == 1 else 1, (adjRow, adjCol)))
        raise Exception("Error: empty queue")

