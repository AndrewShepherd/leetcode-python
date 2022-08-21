from collections import defaultdict

class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        d = defaultdict(lambda: 0)
        for i,v in enumerate(edges):
            d[v] += i
        maxScore = 0
        for edge,score in sorted(d.items()):
            if score > maxScore:
                maxScore = score
                maxEdge = edge
        return maxEdge