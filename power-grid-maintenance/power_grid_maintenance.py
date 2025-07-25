from collections import defaultdict, deque

class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        print('starting')
        d = defaultdict(set)
        for n1, n2 in connections:
            d[n1].add(n2)
            d[n2].add(n1)
        is_online = [True] * (c+1)
        networks = []
        network_indexes = [None] * (c+1)
        for i in range(1, c+1):
            if network_indexes[i] == None:
                new_network = set()
                q = [i]
                while(q):
                    j = q.pop()
                    if not j in new_network:
                        new_network.add(j)
                        for other_node in d[j]:
                            if not other_node in new_network:
                                q.append(other_node)
                        network_indexes[j] = len(networks)
                networks.append(new_network)
        networks = [deque(sorted(list(s))) for s in networks]
        results = []
        for query_type, station_id in queries:
            if query_type == 1:
                if is_online[station_id]:
                    results.append(station_id)
                else:
                    network = networks[network_indexes[station_id]]
                    while network and not is_online[network[0]]:
                        print(f'network = {network}. is_line = {is_online}. popping left')
                        network.popleft()
                        print(f'popped left. network = {network}.')
                    if network:
                        results.append(network[0])
                    else:
                        results.append(-1)
            else:
                is_online[station_id] = False
        return results
        
