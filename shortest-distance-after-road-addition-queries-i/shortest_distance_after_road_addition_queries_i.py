class RangeTreeEmptyNode:

    def __init__(self, range_start, range_end_exclusive):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive

    def block(self, range_start, range_end_exclusive):
        return (self, 0)
    
class RangeTreeFullNode:

    def __init__(self, range_start, range_end_exclusive):
        self.range_start = range_start
        self.range_end_exclusive = range_end_exclusive

    def block(self, range_start, range_end_exclusive):
            

    
class SegmentTreeLeafNode:
    def __init__(self, range_min, range_max_exclusive, index, distance):
        self.range_min = range_min
        self.range_max_exclusive = range_max_exclusive
        self.index = index
        self.distance = distance

    def __len__(self):
        return 1

    def __contains__(self, index):
        return (self.index == index)
    
    def __getitem__(self, index):
        if index == self.index:
            return self.distance
        else:
            raise Exception("GetItem invoked on mismatched leaf node")
        

    def next_greater(self, index):
        if index < self.index:
            return (self.index, self.distance)
        else:
            return None
        
    def get_greatest_less_than_or_equal_to(self, index):
        if index >= self.index:
            return (self.index, self.distance)
        else:
            return None

    def set(self, index, distance):
        if index == self.index:
            self.distance = distance
            return self
        else:
            mid_point = (self.range_max_exclusive + self.range_min) // 2
            left = SegmentTreeEmptyNode(self.range_min, mid_point)
            right = SegmentTreeEmptyNode(mid_point, self.range_max_exclusive)
            if self.index < mid_point:
                left = left.set(self.index, self.distance)
            else:
                right = right.set(self.index, self.distance)
            if index < mid_point:
                left = left.set(index, distance)
            else:
                right = right.set(index, distance)
            return SegmentTreeBranchNode(
                self.range_min,
                self.range_max_exclusive,
                left, 
                right
            )
        
class SegmentTreeBranchNode:
    def __init__(self, range_min, range_max_exclusive, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node
        self.range_min = range_min
        self.range_max_exclusive = range_max_exclusive
        self.mid_point = (range_max_exclusive + range_min) // 2

    def set(self, index, distance):
        if index < self.mid_point:
            self.left_node = self.left_node.set(index, distance)
        else:
            self.right_node = self.right_node.set(index, distance)
        return self

    def next_greater(self, index):
        result = None
        if index < self.mid_point:
            result = self.left_node.next_greater(index)
        if result == None:
            result = self.right_node.next_greater(index)
        return result
    
    def get_greatest_less_than_or_equal_to(self, index):
        result = None
        if index >= self.mid_point: 
            result = self.right_node.get_greatest_less_than_or_equal_to(index)
        if result == None:
            result = self.left_node.get_greatest_less_than_or_equal_to(index)
        return result
        
    def __len__(self):
        return len(self.left_node) + len(self.right_node)
    
    def __getitem__(self, index):
        return self.left_node[index] if index < self.mid_point else self.right_node[index]   


    def __contains__(self, index):
        return index in self.left_node if index < self.mid_point else index in self.right_node      
        
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        edges = defaultdict(set)
        edges[0].add(n-1)
        distances = SegmentTreeEmptyNode(0, n)
        distances = distances.set(0, 0)
        result = []

        def get_distance(node):
            prev_node, prev_distance = distances.get_greatest_less_than_or_equal_to(node)
            return prev_distance + (node - prev_node)

        query_dests = set([r for l,r in queries])
        query_sources = set([l for l,r in queries])

        for l,r in queries:
            if (r - l) > 1:
                edges[l].add(r)
                d_to_l = get_distance(l)
                d_to_r = get_distance(r)
                distances = distances.set(l, d_to_l)
                if d_to_r > d_to_l + 1:
                    distances = distances.set(r, d_to_l + 1)
                    q = [(distances[r], r)]
                    visited = set()
                    while q:
                        distance, source_node = heapq.heappop(q)
                        if source_node in visited:
                            continue
                        visited.add(source_node)
                        if source_node in edges:
                            for dest_node in edges[source_node]:
                                if distances[dest_node] > distance + 1:
                                    distances = distances.set(dest_node, distance + 1)
                                    heapq.heappush(q, (distance + 1, dest_node))
                        next_greater = distances.next_greater(source_node)  
                        if next_greater:
                            gn, gd = next_greater
                            if gn not in visited:
                                gnd = (gn - source_node + distance)
                                if (gn not in distances) or (distances[gn] > gnd):
                                    # Could actually remove it instead
                                    distances = distances.set(gn, gnd)
                                    heapq.heappush(q, (gnd, gn))
            result.append(get_distance(n-1))
        return result
