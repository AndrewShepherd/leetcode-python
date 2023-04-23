from collections import defaultdict

class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        d = defaultdict(set)
        trip_cache = dict()
        for l,r in edges:
            d[l].add(r)
            d[r].add(l)
            trip_cache[(l, r)] = [l, r]
            trip_cache[(r, l)] = [l, r]
        
        # for each trip, calculate the set of nodes:

        def get_nodes_in_trip(a, b):
            if (a == b):
                return [a]
            if (a,b) in trip_cache:
                return trip_cache[(a, b)]
            to_visit = [(a, [a])]
            visited = set()
            while(to_visit):
                node, nodes_in_path = to_visit.pop()
                visited.add(node)
                for adjacent in d[node]:
                    if adjacent in visited:
                        continue
                    new_nodes_in_path = nodes_in_path + [adjacent]
                    trip_cache[(a, adjacent)] = new_nodes_in_path
                    trip_cache[(adjacent, a)] = new_nodes_in_path
                    if (adjacent == b):
                        return new_nodes_in_path
                    to_visit.append((adjacent, new_nodes_in_path))
            return None
        node_costs = defaultdict(lambda: 0)
        for a,b in trips:
            nodes = get_nodes_in_trip(a, b)
            for n in nodes:
                node_costs[n] += price[n]

        total_price_before_halving = sum(node_costs.values())
        best_discount = 0

        def get_best_discount(available_nodes, min_acceptable):
            if not(available_nodes):
                return 0
            amount_we_can_possibly_take_off = sum([node_costs[n] for n in available_nodes]) // 2
            if amount_we_can_possibly_take_off < min_acceptable:
                return 0
            amount_if_we_discount_first = node_costs[available_nodes[0]]//2
            remaining = [n for n in available_nodes[1:] if (n not in d[available_nodes[0]])]
            amount_if_we_discount_first += get_best_discount(remaining, min_acceptable - amount_if_we_discount_first)
            amount_if_we_keep_first = get_best_discount(available_nodes[1:], max(min_acceptable, amount_if_we_discount_first))
            return max(amount_if_we_discount_first, amount_if_we_keep_first)

        all_nodes = [n for n in range(len(price)) if node_costs[n]]
        all_nodes.sort(key=lambda n: 0-node_costs[n])
        best_discount = get_best_discount(all_nodes, 0)
        return total_price_before_halving - best_discount
