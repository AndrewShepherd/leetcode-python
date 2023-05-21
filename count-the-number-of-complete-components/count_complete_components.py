from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adjacencies = defaultdict(set)
        for n1,n2 in edges:
            adjacencies[n1].add(n2)
            adjacencies[n2].add(n1)
        for v in range(n):
            adjacencies[v].add(v)


        def is_complete_connected_components(nodes):
            for i in range(len(nodes) - 1):
                ni = nodes[i]
                for j in range(i+1, len(nodes)):
                    nj = nodes[j]
                    if not nj in adjacencies[ni]:
                        return False
            return True


        visited = [False] * n
        to_visit = set(range(n))
        total_count = 0
        while(to_visit):
            # Find a bunch of connected nodes
            node_set = []
            unvisited_nodes = {to_visit.pop(),}
            while(unvisited_nodes):
                node = unvisited_nodes.pop()
                node_set.append(node)
                if node in to_visit:
                    to_visit.remove(node)
                visited[node] = True
                for dest in adjacencies[node]:
                    if not visited[dest]:
                        unvisited_nodes.add(dest)
            # Is this complete connected component?
            if is_complete_connected_components(node_set):
                total_count += 1
                    
        return total_count