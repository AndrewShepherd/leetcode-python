class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        # breadth first search from 0
        def get_cycle(start_index):
            cycle_list = [start_index]
            this_index = start_index
            while (True):
                next = edges[this_index]
                if next == start_index:
                    return cycle_list
                else:
                    cycle_list.append(next)
                    this_index = next


        result = []
        cycle_length = [None] * len(edges)
        result = [None] * len(edges)
        for i in range(len(edges)):
            if (result[i] != None):
                continue
            stack = [i]
            current = i
            visited = [False] * len(edges)
            while(True):
                visited[current] = True
                next = edges[current]
                if (result[next] != None):
                    result[current] = result[next] + 1
                    while(stack):
                        e = stack.pop()
                        if result[e] == None:
                            result[e] = 1 + result[edges[e]]  
                    break                 
                if visited[next]:
                    cycle = get_cycle(next)
                    for e in cycle:
                        result[e] = len(cycle)
                    while(stack):
                        e = stack.pop()
                        if result[e] == None:
                            result[e] = 1 + result[edges[e]]
                    break
                else:
                    stack.append(current)
                    current = next

        return result

