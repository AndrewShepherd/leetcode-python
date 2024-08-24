from functools import cache
from collections import defaultdict, deque
import queue


class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        edge_lookup = defaultdict(set)
        all_nodes = set()

        for f,t in edges:
            edge_lookup[f].add(t)
            edge_lookup[t].add(f)
            all_nodes.add(f)
            all_nodes.add(t)

        tree_edges = defaultdict(set)
        q = deque([0])
        visited = set()
        while(q):
            n = q.popleft()
            for c in edge_lookup[n]:
                if c in visited:
                   continue
                tree_edges[n].add(c)
                q.append(c)
            visited.add(n)
        
        @cache
        def get_size(n):
            t = 1
            for d in tree_edges[n]:
                t += get_size(d)
            return t

        @cache 
        def is_good(n):
            sizes = [get_size(d) for d in tree_edges[n]]
            return len(set(sizes)) < 2

        return len([n for n in all_nodes if is_good(n)])



