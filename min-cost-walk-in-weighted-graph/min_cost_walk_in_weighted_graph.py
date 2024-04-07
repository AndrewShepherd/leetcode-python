from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        node_set_lookup = [None] * n
        node_weight = [0xFFFFFFFF] * n
        
        adjacencies = defaultdict(set)
        for n1,n2,w in edges:
            adjacencies[n1].add(n2)
            adjacencies[n2].add(n1)
            node_weight[n1] &= w
            node_weight[n2] &= w

        # Now create the node sets
        unassigned_nodes = set(range(n))
        set_weights = defaultdict(lambda:0xFFFFFFFF)
        set_id = 0
        
        while unassigned_nodes:
            to_do = [unassigned_nodes.pop()]
            while(to_do):
                node = to_do.pop()
                if(node_set_lookup[node] == None):
                    node_set_lookup[node] = set_id
                    set_weights[set_id] &= node_weight[node]
                    for adjacent in adjacencies[node]:
                        if node_set_lookup[adjacent] == None:
                            to_do.append(adjacent)
            set_id += 1

        result = []
        for f,t in query:
            if f == t:
                result.append(0)
                continue
            set_id = node_set_lookup[f]
            if set_id != node_set_lookup[t]:
                result.append(-1)
            else:
                result.append(set_weights[set_id])

        return result
