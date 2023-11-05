from collections import defaultdict


def generate_sorted_list(relationships, n: int) -> list[tuple]:


    visited = [False] * n
    visited[0] = True
    sorted_list = [(0,None)]
    i = 0
    while i < len(sorted_list):
        node, parent = sorted_list[i]
        child_indexes = [c for c in relationships[node] if not visited[c]]
        for c in child_indexes:
            visited[c] = True
            sorted_list.append((c, node))
        i += 1
    return sorted_list

class Solution:
    def maximumScoreAfterOperations(self, edges: list[list[int]], values: list[int]) -> int:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        sorted_list = generate_sorted_list(graph, len(values))
        # (sum_total, best_without_constraint)
        results = [None] * len(values)

        
        while(sorted_list):
            node_index, node_parent = sorted_list.pop()
            children = [c for c in graph[node_index] if results[c] != None]
            child_sum_total = sum([results[c][0] for c in children])
            child_with_constraints = sum([results[c][1] for c in children])
            this_sum_total = values[node_index] + child_sum_total
            if len(children) == 0:
                this_with_constraints = 0
            else:
                this_with_constraints = max(child_sum_total, values[node_index] + child_with_constraints)
            results[node_index] = (this_sum_total, this_with_constraints)
        
        return results[0][1]
        

        return 0
        
