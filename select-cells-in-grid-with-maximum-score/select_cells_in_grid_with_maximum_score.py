from collections import defaultdict

def remove_value(rows, value):
    empty_row_indexes = []
    for i, r in enumerate(rows):
        if value in r:
            index_to_remove = r.index(value)
            rows[i] = r[:index_to_remove] + r[index_to_remove+1:]
            if len(rows[i]) == 0:
                empty_row_indexes.append(i)
    for i in reversed(empty_row_indexes):
        del rows[i]
    rows.sort(key= lambda r:(0-r[0]))
    return rows

def remove_row_and_value(rows, row, value):
    index_to_remove = rows.index(row)
    rows = rows[:index_to_remove] + rows[index_to_remove+1:]
    return remove_value(rows, value)

def generate_values_by_rows(rows):
    d = defaultdict(list)
    for r in rows:
        for c in r:
            d[c].append(r)
    return sorted(d.items(), key=lambda item:0-item[0])

def solve_recursively(rows: list[list[int]], available_additions):
    rows = sorted(rows, key= lambda r:(0-r[0]))
    result = 0
    while (available_additions and rows):
        l = generate_values_by_rows(rows)
        available_additions = min([available_additions, len(rows), len(l)])
        rows_with_one = [rows[i] for i in range(available_additions) if len(rows[i]) == 1]
        if rows_with_one:
            row = rows_with_one[0]
            value = row[0]
            result += value
            available_additions -= 1
            rows = remove_row_and_value(rows, row, value)
            continue
        # Out of the first required, are there any numbers that appear in all of them?
        appearing_in_all = [value for value,rows in l[:available_additions] if len(rows) >= available_additions]
        if (appearing_in_all):
            available_additions -= 1
            result += appearing_in_all[0]
            rows = remove_value(rows, appearing_in_all[0])
            continue
        top_value = l[0][0]
        best_result = 0
        for row in l[0][1]:
            new_rows = remove_row_and_value(rows, row, top_value)
            this_result = solve_recursively(new_rows, available_additions-1) + top_value
            best_result = max(best_result, this_result)
        return best_result + result
    return result


class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        rows = [ 
                sorted(set(r), key=lambda n:0-n)
                for r in grid
            ]
        
        return solve_recursively(rows, len(rows))
        

        

 
