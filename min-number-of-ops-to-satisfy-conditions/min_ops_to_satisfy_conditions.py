from collections import Counter;

class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        column_height = len(grid)
        column_count = len(grid[0])
        possibilities = [0] * 10
        for column in range(column_count):
            values = Counter([row[column] for row in grid])
            p2 = [None] * 10
            for i in range(10):
                p2[i] = column_height - values[i] + min([n for i2,n in enumerate(possibilities) if i2 != i])
            possibilities = p2
        return min(possibilities)
