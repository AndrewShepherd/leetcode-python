from bisect import *

class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        first_indexes = [r[0] for r in matrix]
        rbr = bisect_right(first_indexes, target)
        if rbr == len(first_indexes):
            return False
        if rbr < len(first_indexes) and first_indexes[rbr] == target:
            return True

        row_index = rbl - 1
        column = matrix[row_index]
        column_bisect_left_result = bisect_left(column, target)
        return column_bisect_left_result < len(column) and column[column_bisect_left_result] == target

