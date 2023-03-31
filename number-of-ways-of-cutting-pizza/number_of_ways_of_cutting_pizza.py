from functools import cache

modulo = 1000000007

def output_pizza(pizza: list[str]):
    print("\n*** pizza ***")
    for p in pizza:
        print(p)
    print("************")

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        @cache
        def number_of_ways(start_row_index, start_col_index, remaining_cuts, tab):
            if remaining_cuts == 0:
                return 1
            rows_with_values = set()
            cols_with_values = set()
            for i in range(start_row_index, len(pizza)):
                for j in range(start_col_index, len(pizza[i])):
                    if pizza[i][j] == 'A':
                        rows_with_values.add(i)
                        cols_with_values.add(j)
            rows_with_values = sorted(list(rows_with_values))
            cols_with_values = sorted(list(cols_with_values))
            result = 0
            for row_index in rows_with_values[:-1]:
                result = result + number_of_ways(row_index + 1, start_col_index, remaining_cuts - 1, tab + 3)
            for col_index in cols_with_values[:-1]:
                result = result + number_of_ways(start_row_index, col_index + 1, remaining_cuts - 1, tab + 3)
            print(f"{' '*tab}number_of_ways({start_row_index}, {start_col_index}, {remaining_cuts}) returns {result}")
            return result % modulo
        output_pizza(pizza)
        return number_of_ways(0, 0, k - 1, 0)
                

