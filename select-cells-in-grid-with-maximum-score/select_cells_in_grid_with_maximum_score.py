class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        rows = [ 
                sorted(set(r), key=lambda n:0-n)
                for r in grid
            ]
        rows.sort(key= lambda r:(len(r), 0-r[0]))
        max_possible_values = [r[0] for r in rows]
        for i in range(len(max_possible_values)-2, -1, -1):
            max_possible_values[i] += max_possible_values[i+1]
    
        used = [False] * 101 

        def best_result(row_index, min_threshold):
            if row_index == len(rows):
                return 0
            if max_possible_values[row_index] < min_threshold:
                return None
            result = None
            for n in rows[row_index]:
                if used[n]:
                    continue
                used[n] = True
                new_min_threshold = 0
                if result == None:
                    new_min_threshold = min_threshold - n
                else:
                    new_min_threshold = max(min_threshold, result) - n
                sub_result = best_result(row_index+1, new_min_threshold)
                used[n] = False
                if (sub_result == None):
                    continue
                this_result = n + sub_result
                result = this_result if result == None else max(this_result, result)
            return result

        return best_result(0, 0)
