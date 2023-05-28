from collections import defaultdict

def get_all_paths(distances, destination):
    path_length, via = distances[destination]
    if path_length == 0:
        return [destination]
    else:
        return get_all_paths(distances, via) + [destination]

class Solution:
    def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:

        adjustable_edge_indexes = set()
        adjacencies = defaultdict(list)
        for i,e in enumerate(edges):
            l,r,w = e
            if w == -1:
                e[2] = 1
                adjustable_edge_indexes.add(i)
            adjacencies[l].append((r, i))
            adjacencies[r].append((l, i))

        def get_shortest_path():
            distances = [None] * n
            distances[source] = (0, []) # Weight, all the nodes you can get there via
            visited = [False] * n
            while( True):
                closest_node = None
                for i, v in enumerate(distances):
                    if visited[i]:
                        continue
                    if v == None:
                        continue
                    if closest_node == None:
                        closest_node = i
                    elif distances[i][0] < distances[closest_node][0]:
                        closest_node = i
                if closest_node == None:
                    break
                node = closest_node
                if node == destination:
                    break
                path_length, via = distances[node]
                visited[node] = True
                for adjacent_node, edge_index in adjacencies[node]:
                    l,r,w = edges[edge_index]
                    new_distance = path_length + w
                    if distances[adjacent_node] == None:
                        distances[adjacent_node] = (new_distance, node)
                    else:
                        existing_distance, existing_node = distances[adjacent_node]
                        if existing_distance == new_distance:
                            None
                        elif existing_distance > new_distance:
                            distances[adjacent_node] = (new_distance, node)
            return get_all_paths(distances, destination)

        def get_edge_indexes(path):
            for f,t in zip(path[:-1], path[1:]):
                edge_index = [e for r,e in adjacencies[f] if r==t][0]
                yield edge_index

        at_least_one = False
        while(True):
            p = get_shortest_path()
            edges_to_adjust = []
            total_positive = 0
            edge_indexes = set(get_edge_indexes(p))
            for edge_index in edge_indexes:
                edge = edges[edge_index]
                if edge_index in adjustable_edge_indexes:
                    edges_to_adjust.append(edge)
                total_positive += edge[2]
            if total_positive > target:
                return []
            elif total_positive == target:
                return edges
            else:
                values_to_assign = target - total_positive
                if values_to_assign > 0 and len(edges_to_adjust) == 0:
                    return []
                edges_to_adjust[0][2] += values_to_assign
                # All the remaining edges can be upped to target
                for edge_index in adjustable_edge_indexes.difference(edge_indexes):
                    edges[edge_index][2] = target



