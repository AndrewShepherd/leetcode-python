from functools import cache

modulo = 1000000007

def output_pizza(pizza: list[str]):
    print("\n*** pizza ***")
    for p in pizza:
        print(p)
    print("************")

# A board node will contain the following:

# The values for each of the range of prices
# Whether this row is compatible (going by all of the colum values for this one and to the right)
# Whether this column is compatible
class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        empty = ([0] * k, False, False)
        board = [
            [empty] * (len(pizza[0]) + 1)
            for _ in range(len(pizza) + 1)
        ]
        for row_index, s in reversed(list(enumerate(pizza))):
            for col_index, c in reversed(list(enumerate(s))):
                values = [0] * k
                row_has_it = False
                col_has_it = False
                if c == 'A':
                    values[0] = 1
                    row_has_it = True
                    col_has_it = True
                for right_col_index in range(col_index + 1, len(board[row_index])):
                    values_2, row_has_it_2, col_has_it_2 = board[row_index][right_col_index]
                    if values_2[0] == 1:
                        values[0] = 1
                    row_has_it |= row_has_it_2
                for lower_row_index in range(row_index + 1, len(board)):
                    values_2, row_has_it_2, col_has_it_2 = board[lower_row_index][col_index]
                    if values_2[0] == 1:
                        values[0] = 1
                    col_has_it |= col_has_it_2
                can_cut_vertically = col_has_it
                board[row_index][col_index] = (values, row_has_it, col_has_it)

                for col_index_2 in range(col_index, len(s)):
                    values_2, row_has_it_2, col_has_it_2 = board[row_index][col_index_2]
                    can_cut_vertically |= col_has_it_2
                    if can_cut_vertically:
                        values_to_right = board[row_index][col_index_2+1][0]
                        for i in range(1, k):
                            values[i] = (values[i] + values_to_right[i-1]) % modulo
                can_cut_horizontally = row_has_it
                for row_index_2 in range(row_index, len(pizza)):
                    values_2, row_has_it_2, col_has_it_2 = board[row_index_2][col_index]
                    can_cut_horizontally |= row_has_it_2
                    if can_cut_horizontally:
                        values_below = board[row_index_2+1][col_index][0]
                        for i in range(1, k):
                            values[i] = (values[i] + values_below[i-1]) % modulo
        return board[0][0][0][-1]
                

