from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        edges = defaultdict(set)
        for n1,n2 in dislikes:
            if n1 != n2:
                edges[n1].add(n2)
                edges[n2].add(n1)
        while (edges):
            firstNode = list(edges.keys())[0]
            q = [firstNode]
            included, excluded = { firstNode }, set()
            while q:
                n = q.pop()
                if not n in edges:
                    continue
                nEdges = edges.pop(n)
                q2 = []
                for n2 in nEdges:
                    if n2 in excluded:
                        return False
                    q2.append(n2)
                    included.add(n2)
                    edges[n2].remove(n)
                    if not edges[n2]:
                        del edges[n2]
                q = q2
                included,excluded = excluded,included
        return True
