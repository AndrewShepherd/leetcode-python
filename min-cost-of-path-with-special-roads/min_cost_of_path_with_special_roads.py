class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        all_points = set()
        all_points.add((start[0], start[1]))
        all_points.add((target[0], target[1]))
        for s1,s2,t1,t2,dist in specialRoads:
            all_points.add((s1, s2))
            all_points.add((t1, t2))
        point_to_index = dict()
        all_points = list(all_points)
        for i,p in enumerate(all_points):
            point_to_index[p] = i
        
        from_to = [[None] * len(all_points) for _ in all_points]
        # Fill with the default lengths
        for i in range(len(all_points)):
            pi = all_points[i]
            for j in range(len(all_points)):
                pj = all_points[j]
                dist = abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])
                from_to[i][j] = dist

        # Add the special roads
        for s1,s2,t1,t2,dist in specialRoads:
            iFrom = point_to_index[s1,s2]
            iTo = point_to_index[t1,t2]
            from_to[iFrom][iTo] = min(from_to[iFrom][iTo], dist)

        # Implement dijkstra
        start_index = point_to_index[tuple(start)]
        target_index = point_to_index[tuple(target)]

        distances = from_to[start_index][:]


        visited = set()
        while(True):
            closest_unvisited_distance, closest_unvisited_index = min([
                (distance, i) 
                    for i,distance 
                    in enumerate(distances) 
                    if i not in visited
            ])
            if closest_unvisited_index == target_index:
                return closest_unvisited_distance
            for i,d in enumerate(from_to[closest_unvisited_index]):
                distance_from_start = closest_unvisited_distance + d
                distances[i] = min(distances[i], distance_from_start)
            visited.add(closest_unvisited_index)

        return 0
