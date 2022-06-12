class Solution:
    def minPathCost(self, grid, moveCost) -> int:
        row_cost = grid[-1][:]
        for row_index in range(len(grid)-2, -1, -1):
            above_row_cost = grid[row_index][:]
            for column_index in range(len(above_row_cost)):
                move_cost_entry = moveCost[grid[row_index][column_index]]
                travel_costs = [row_cost[ci] + move_cost_entry[ci] for ci in range(len(above_row_cost))]
                travel_cost = min(travel_costs)
                above_row_cost[column_index] += travel_cost
            row_cost = above_row_cost
        return min(row_cost)