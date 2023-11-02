from collections import defaultdict
from functools import cache
from math import floor

def maxify(result):
    m = 0
    for i in range(len(result)-1, -1, -1):
        m = max(m, result[i])
        result[i] = m
    return result

def safe_get(l, i):
    if i < len(l):
        return l[i]
    else:
        return 0

def add_lists(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    max_len = max(len1, len2)
    return [safe_get(l1, i) + safe_get(l2, i) for i in range(max_len)] 

def generate_sorted_list(edges: list[list[int]], n: int) -> list[tuple]:
    relationships = defaultdict(list)

    for node1, node2 in edges:
        relationships[node1].append(node2)
        relationships[node2].append(node1)

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
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        sorted_list = generate_sorted_list(edges, len(coins))
        dp = [None] * len(coins)

        while(sorted_list):
            node, parent = sorted_list.pop()
            existing = [] if dp[node] == None else dp[node]
            
            these_scores = []
            these_coins = coins[node]
            i = 0
            while (True):
                this_value = max(
                    these_coins - k + safe_get(existing, i),
                    floor(these_coins / 2) + safe_get(existing, i + 1)
                )
                if this_value == 0:
                    break
                these_scores.append(this_value)
                these_coins = floor(these_coins / 2)
                i += 1

            if (parent == None):
                return these_scores[0] if len(these_scores) else 0
            else:
                if dp[parent] == None:
                    dp[parent] = these_scores
                else:
                    dp[parent] = add_lists(dp[parent], these_scores)
