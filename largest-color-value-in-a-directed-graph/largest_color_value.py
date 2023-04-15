from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        if not edges:
            return 1
        fromTo = [0] * len(colors)
        toFrom = defaultdict(set)
        for f,t in edges:
            fromTo[f] += 1
            toFrom[t].add(f)
        maxFrom = [[0]*26 for _ in range(len(colors))]
        best_value = 0
        counted = 0
        to_process = [i for i,v in enumerate(fromTo) if v == 0]
        while(to_process):
            end_node = to_process.pop()
            counted += 1
            dest_values = maxFrom[end_node]
            dest_values[ord(colors[end_node]) - ord('a')] += 1
            best_value = max(best_value, max(dest_values))
            for source_node in toFrom[end_node]:
                source_values = maxFrom[source_node]
                for i,v in enumerate(dest_values):
                    source_values[i] = max(source_values[i], v)
                fromTo[source_node] -= 1
                if fromTo[source_node] == 0:
                    to_process.append(source_node)
        if counted < len(colors):
            return -1

        return best_value

