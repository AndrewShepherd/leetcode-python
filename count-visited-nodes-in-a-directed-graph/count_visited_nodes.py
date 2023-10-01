class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        result = [None] * len(edges)
        for i in range(len(edges)):
            if (result[i] != None):
                continue
            stack = [i]
            d = dict()
            d[i] = len(stack) - 1
            while(True):
                next = edges[stack[-1]]
                if result[next] != None:
                    for e in reversed(stack):
                        result[e] = result[edges[e]] + 1
                    break
                elif next in d:
                    # We have a cycle
                    sIndex = d[next]
                    cycle_length = len(stack) - sIndex
                    for j in range(sIndex, len(stack)):
                        result[stack[j]] = cycle_length
                    for j in range(sIndex-1, -1, -1):
                        result[stack[j]] = result[edges[stack[j]]] + 1
                    break
                else:
                    stack.append(next)
                    d[next] = len(stack) - 1

        return result

