import math




def solve(n, edges):
    visited = set()
    distances = [None] * n
    distances[0] = 0
    q = [0]
    while(q):
        min_index = 0
        for i in range(1, len(q)):
            if distances[q[i]] < distances[q[min_index]]:
                min_index = i
        node = q[min_index]
        del q[min_index]
        if node in visited:
            continue
        visited.add(node)
        dn = distances[node]
        if node in edges:
            for dest in edges[node]:
                if dest in visited:
                    continue
                distances[dest] = dn + 1 if distances[dest] == None else min(distances[dest], dn + 1)
                q.append(dest)
    return distances[-1]


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        edges = dict()

        for i in range(n-1):
            edges[i] = [i+1]

        result = []
        for l,r in queries:
            edges[l].append(r)
            result.append(solve(n, edges))
        return result
