from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        flattened = [None] * (n*m)
        for row in range(n):
            for col in range(m):
                flattened[row*m + col] = (mat[row][col], row, col)
        flattened.sort(key=lambda t:0-t[0])
        max_for_row = [0] * n
        max_for_col = [0] * m

        working_row = defaultdict(int)
        working_col = defaultdict(int)
        for index, (value, row, col) in enumerate(flattened):
            working_row[row] = max([working_row[row], max_for_row[row] + 1, max_for_col[col] + 1])
            working_col[col] = max([working_col[col], max_for_col[col] + 1, max_for_row[row] + 1])
            if index == len(flattened) - 1 or flattened[index+1][0] != value:
                for k in working_row.keys():
                    max_for_row[k] = working_row[k]
                for k in working_col.keys():
                    max_for_col[k] = working_col[k]
                working_row.clear()
                working_col.clear()
        return max(max_for_row)
