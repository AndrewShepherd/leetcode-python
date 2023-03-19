class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        if (grid[0][0]) != 0:
            return False
        cells = [None] * (len(grid) * len(grid))
        for rowIndex, row in enumerate(grid):
            for cellIndex, cellValue in enumerate(grid[rowIndex]):
                if cells[cellValue] != None:
                    return False
                cells[cellValue] = (rowIndex, cellIndex)
        for i in range(1, len(cells)):
            prev_cell, this_cell = cells[i-1], cells[i]
            j1 = abs(prev_cell[0] - this_cell[0])
            j2 = abs(prev_cell[1] - this_cell[1])
            is_valid = (j1,j2) == (1,2) or (j1,j2) == (2,1)
            if not is_valid:
                return False
        return True
