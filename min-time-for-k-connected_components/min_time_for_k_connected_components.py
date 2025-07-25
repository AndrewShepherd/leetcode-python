from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: list[list[int]], k: int) -> int:

        def test(min_time):
            d = defaultdict(set)
            for (u, v, t) in edges:
                if t <= min_time:
                    continue
                d[u].add(v)
                d[v].add(u)
            included = [False] * n
            network_count = 0
            for node_id in range(n):
                if (included[node_id]):
                    continue
                network_count += 1
                if network_count == k:
                    return True
                q = [node_id]
                while(q):
                    this_node = q.pop()
                    if (included[this_node]):
                        continue
                    included[this_node] = True
                    q.extend([j for j in d[this_node] if not included[j]])
            return False

        all_times = [0] + sorted(set([t for (u,v,t) in edges]))
        range_start = 0
        range_end_inclusive = len(all_times) - 1
        while(range_start < range_end_inclusive):
            range_mid = (range_start + range_end_inclusive)//2
            if (test(all_times[range_mid])):
                range_end_inclusive = range_mid
            else:
                range_start = range_mid + 1
        return all_times[range_start]
