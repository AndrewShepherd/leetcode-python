from collections import defaultdict
from smtplib import LMTP

class Solution:
    def countPaths(self, grid) -> int:
        paths = [[0] * len(row) for row in grid]
        d = defaultdict(list)
        for (r, row) in enumerate(grid):
            for (c, val) in enumerate(row):
                d[val].append((r, c))
        values =list(d.keys())
        values.sort(key = lambda x:-x)
        for v in values:
            for row, col in d[v]:
                others = []
                if row > 0 and grid[row-1][col] > v:
                    others.append(paths[row-1][col])
                if row < len(grid) - 1 and grid[row+1][col] > v:
                    others.append(paths[row+1][col])
                if col > 0 and grid[row][col-1] > v:
                    others.append(paths[row][col-1])
                if col < len(grid[0]) - 1 and grid[row][col+1] > v:
                    others.append(paths[row][col+1])
                paths[row][col] = 1 + sum(others)
        return sum([sum(r) for r in paths]) % 1000000007



