from collections import defaultdict
from functools import cache
from math import floor

class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        relationships = defaultdict(list)

        for node1, node2 in edges:
            relationships[node1].append(node2)
            relationships[node2].append(node1)
        
        visited = [False] * len(coins)
        @cache
        def best_result(node_index, divisions):
            visited[node_index] = True
            adjacent_nodes = [i for i in relationships[node_index] if not visited[i]]
            child_results_divisions = []
            if divisions < 14:
                child_results_divisions = [best_result(child_index, divisions+1) for child_index in adjacent_nodes]
            child_results_division = sum(child_results_divisions)
            no_divisions = [best_result(child_index, divisions) for child_index in adjacent_nodes]
            child_results_no_division = sum(no_divisions)
            visited[node_index] = False
            return max(
                floor(coins[node_index]/(2**divisions)) - k + child_results_no_division,
                floor(coins[node_index]/(2**(divisions+1))) + child_results_division
            )
        
        return best_result(0, 0)