from collections import Counter
from math import inf;

def is_y_coordinate(rowIndex, colIndex, n):
    if (rowIndex >= n//2):
        return colIndex == n//2
    else:
        return rowIndex == colIndex or rowIndex == n-colIndex-1


class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        y = []
        nonY = []
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if is_y_coordinate(row_index, col_index, len(grid)):
                    y.append(value)
                else:
                    nonY.append(value)
        cY = Counter(y)
        cNonY = Counter(nonY)

        tY = (cY[0], cY[1], cY[2])
        tNonY = (cNonY[0], cNonY[1], cNonY[2])

        best_result = inf

        for i in range(3):
            i_transformations = sum([n for index,n in enumerate(tY) if index != i])
            for j in range(3):
                if i == j:
                    continue
                j_transformations = sum([n for index, n in enumerate(tNonY) if index != j])
                best_result = min(best_result, i_transformations + j_transformations)
        return best_result

        return 0
        
