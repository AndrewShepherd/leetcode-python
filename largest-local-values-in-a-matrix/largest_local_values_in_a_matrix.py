class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        result = [[None]*(n-2) for _ in range(n-2)]
        for r in range(len(result)):
            for c in range(len(result[r])):
                maxValue = 0
                for r2 in range(r,r+3):
                    for c2 in range(c, c+3):
                        maxValue = max(grid[r2][c2], maxValue)
                result[r][c] = maxValue
        return result