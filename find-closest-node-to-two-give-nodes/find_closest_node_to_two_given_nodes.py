import math


def generateDistances(edges, node):
    distances = [math.inf] * len(edges)
    distances[node] = 0
    l = 1
    while(True):
        next = edges[node]
        if next == -1:
            return distances
        if distances[next] != math.inf:
            return distances
        distances[next] = min(distances[next], l)
        l += 1
        node = next

class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int) -> int:
        node1Distances = generateDistances(edges, node1)
        node2Distances = generateDistances(edges, node2)
        bestResult = math.inf
        bestIndex = -1
        for i, (d1, d2) in enumerate(zip(node1Distances, node2Distances)):
            if d1 != math.inf and d2 != math.inf and max(d1, d2) < bestResult:
                bestResult = max(d1, d2)
                bestIndex = i
        return bestIndex

