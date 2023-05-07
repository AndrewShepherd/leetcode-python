class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        leaf_count = (n+1)//2
        leaf_costs = [0] * leaf_count
        for i in range(len(leaf_costs)):
            end_index = n - leaf_count + i
            while(end_index):
                leaf_costs[i] += cost[end_index]
                end_index = (end_index-1)//2

        target = max(leaf_costs)

        increment_tree = [0] * n


        for i,v in enumerate(leaf_costs):
            end_index = n - leaf_count + i
            increment_tree[end_index] = target - v

        for i in range(n-1, -1, -1):
            j = i*2 + 1
            k = i*2 + 2
            if k < len(increment_tree):
                m = min(increment_tree[j], increment_tree[k])
                increment_tree[i] = m
                increment_tree[j] -= m
                increment_tree[k] -= m
        
        return sum(increment_tree)
