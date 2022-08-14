from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges, restricted) -> int:
        restricted = set(restricted)
        edgelookup = defaultdict(set)
        for e in edges:
            if e[0] not in restricted and e[1] not in restricted:
                edgelookup[e[0]].add(e[1])
                edgelookup[e[1]].add(e[0])
        visited = [False]*n
        reachable = set([0])
        toTryNext = [0]
        while(toTryNext):
            n = toTryNext.pop()
            visited[n] = True
            for q in edgelookup[n]:
                if not visited[q] and q not in reachable:
                    reachable.add(q)
                    toTryNext.append(q)
        return len(reachable)
