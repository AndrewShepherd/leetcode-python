class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        reachable_cells = [True] * len(grid)
        steps = 0
        for col in range(1, len(grid[0])):
            next_column = [False] * len(grid)
            for row in range(len(grid)):
                this_value = grid[row][col]
                for test_row in [row-1, row, row+1]:
                    if 0 <= test_row < len(grid) and reachable_cells[test_row] and grid[test_row][col-1] < this_value:
                        next_column[row] = True
            if len([v for v in next_column if v]):
                steps += 1
                reachable_cells = next_column
            else:
                break
        return steps
