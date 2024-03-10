class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        sums = [[0] * len(r) for r in grid]
        running_count= 0
        for rIndex, row in enumerate(grid):
            for cIndex, value in enumerate(row):
                accumulation = value
                if rIndex > 0:
                    accumulation += sums[rIndex-1][cIndex]
                if cIndex > 0:
                    accumulation += sums[rIndex][cIndex-1]
                if rIndex > 0 and cIndex > 0:
                    accumulation -= sums[rIndex-1][cIndex-1]
                sums[rIndex][cIndex] = accumulation
                if accumulation <= k:
                    running_count += 1
                else:
                    break
        return running_count
