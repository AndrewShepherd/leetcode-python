ROW = 0
COL = 1

class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        remaining_rows = set(range(n))
        remaining_cols = set(range(n))

        total = 0
        for type,index,val in reversed(queries):
            if type == ROW:
                if index in remaining_rows:
                    total += val * len(remaining_cols)
                    remaining_rows.remove(index)
            else:
                if index in remaining_cols:
                    total += val * len(remaining_rows)
                    remaining_cols.remove(index)
        
        return total
