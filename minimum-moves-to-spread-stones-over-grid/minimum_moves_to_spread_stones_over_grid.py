import math


def solve_recursively(too_many, empty) -> int:
    if not empty:
        return 0
    empty_row, empty_col = empty[-1]
    best_result = math.inf
    for index, (source_row, source_col, stone_count) in enumerate(too_many):
        if stone_count == 1:
            raise Exception("This should not have happened!")
        distance = abs(source_row - empty_row) + abs(source_col - empty_col)
        if stone_count > 2:
            new_too_many = too_many[:index] + [(source_row, source_col, stone_count - 1)] + too_many[index+1:]
        else:
            new_too_many = too_many[:index] + too_many[index+1:]
        best_result = min(best_result, distance + solve_recursively(new_too_many, empty[:-1]))
    return best_result


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        too_many = []
        empty = []
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col > 1:
                    too_many.append((row_index, col_index, col))
                elif col == 0:
                    empty.append((row_index, col_index))        
        if not empty:
            return 0
        return solve_recursively(too_many, empty)
        
