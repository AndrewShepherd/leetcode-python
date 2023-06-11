class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        
        def top_left_indexes(r,c):
            while(r > 0 and c > 0):
                r -= 1
                c -= 1
                yield (r,c)
                
        def bottom_right_indexes(r, c):
            while (True):
                r += 1
                c += 1
                if r >= m or c >= n:
                    break
                yield (r, c)
                
        result = [[None] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                d1 = set([grid[r][c] for (r,c) in top_left_indexes(row, col)])
                d2 = set([grid[r][c] for (r,c) in bottom_right_indexes(row, col)])
                result[row][col] = abs(len(d1) - len(d2))
        return result
