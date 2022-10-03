offsets = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 1),
    (2, 0),
    (2, 1),
    (2, 2)
]


class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        maxSum = -1
        for rowIndex in range(len(grid)-2):
            for colIndex in range(len(grid[rowIndex])-2):
                thisSum = 0
                for x,y in offsets:
                    thisSum += grid[rowIndex+x][colIndex+y]
                maxSum = max(maxSum, thisSum)
        return maxSum
