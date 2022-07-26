def getColumns(grid):
    for cIndex in range(len(grid[0])):
        yield [r[cIndex] for r in grid]

class Solution:
    def equalPairs(self, grid) -> int:
        t = 0
        rowsSorted = sorted(grid)
        for c in getColumns(grid):
            t += len([m for m in rowsSorted if c == m])
        return t