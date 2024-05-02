from collections import defaultdict
import heapq
import math

class NodeStatus:
    def __init__(self, visited = False, edges = [], weight = math.inf):
        self.visited = visited
        self.edges = edges
        self.weight = weight

    def mark_as_visited(self):
        return NodeStatus(True, self.edges, self.weight)

    
ZeroNodeStatus = NodeStatus(False, [], 0)
UnreachedNodeStatus = NodeStatus()


class Solution:
    def findAnswer(self, n: int, edges: list[list[int]]) -> list[bool]:
        edge_lookup = defaultdict(list)
        for i,(n1,n2,w) in enumerate(edges):
            edge_lookup[n1].append((n2, i, w))
            edge_lookup[n2].append((n1, i, w))

        node_statuses = [ZeroNodeStatus] + [UnreachedNodeStatus] * (n-1)
        # to_process_element = (weight, node)
        to_process = [(0, 0)]
        

        while(to_process):
            weight, node = heapq.heappop(to_process)
            node_statuses[node] = node_statuses[node].mark_as_visited()
            for destination_node, edge_index, edge_weight in edge_lookup[node]:
                destination_node_status = node_statuses[destination_node]
                if destination_node_status.visited:
                    continue
                new_weight = edge_weight + weight
                

                if destination_node_status.weight > new_weight:
                    destination_node_status = destination_node_status.setWeight(new_weight)  sum_totals[destination_node] = (new_weight, edges_in_shortest_path + [edge_index])
                elif existing_weight == new_weight:
                    _, node_list = sum_totals[destination_node]
                    node_list.extend(edges_in_shortest_path + [edge_index])
                heapq.heappush(to_process, (new_weight, destination_node, sum_totals[destination_node][1]))
        if sum_totals[-1] == None:
            return [False] * len(edges)
        w,edge_indexes = sum_totals[-1]
        edge_indexes = set(edge_indexes)

        return [i in edge_indexes for i in range(len(edges))]
