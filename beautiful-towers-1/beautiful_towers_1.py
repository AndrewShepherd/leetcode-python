

class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        values_and_indexes = sorted([(n, i) for i,n in enumerate(maxHeights)], key=lambda t:0-t[0])
        best_result = 0
        downward_cache = [(None, None)] * len(maxHeights)
        def calculate_downward(start_index, min_acceptable_result):
            this_result = 0
            current_height = maxHeights[start_index]
            to_calculate = []
            running_score = 0
            for i in range(start_index, -1, -1):
                current_height = min(current_height, maxHeights[i])
                lookup_node = (i, current_height)
                if (downward_cache[i][0] == current_height):
                    this_result = downward_cache[i][1]
                    break
                else:
                    running_score += current_height
                    best_possible_result = running_score + (i+1) * current_height
                    if (best_possible_result < min_acceptable_result):
                        return None
                    to_calculate.append(lookup_node)
            while to_calculate:
                lookup_node = to_calculate.pop()
                i, h = lookup_node
                this_result += min(h, maxHeights[i])
                downward_cache[i] = (h, this_result)
            return this_result

        
        upward_cache = [(None, None)] * len(maxHeights)
        def calculate_upward(start_index, min_acceptable_result):
            this_result = 0
            current_height = maxHeights[start_index]
            to_calculate = []
            running_score = 0
            for i in range(start_index, len(maxHeights)):
                current_height = min(current_height, maxHeights[i])
                lookup_node = (i, current_height)
                if (upward_cache[i][0] == current_height):
                    this_result = upward_cache[i][1]
                    break
                else:
                    running_score += current_height
                    best_possible_result = running_score + (len(maxHeights) - i - 1) * current_height
                    if best_possible_result <= min_acceptable_result:
                        return None
                    to_calculate.append(lookup_node)
            while to_calculate:
                lookup_node = to_calculate.pop()
                i, h = lookup_node
                this_result += min(h, maxHeights[i])
                upward_cache[i] = (h, this_result)
            return this_result


        for value, index  in values_and_indexes:
            if (value * len(values_and_indexes) <= best_result):
                break
            best_possible_upward_result = (len(values_and_indexes) - index - 1) * value
            required_minimum = best_result - best_possible_upward_result + 1

            downward_result = calculate_downward(index, required_minimum)
            if (downward_result == None):
                continue
            best_possible_result = downward_result + (len(values_and_indexes) - index - 1) * value
            if best_possible_result <= best_result:
                continue


            required_minimum = best_result - downward_result + value
            upward_result = calculate_upward(index, required_minimum)
            if upward_result == None:
                continue
            this_result = downward_result + upward_result - value
            best_result = max(this_result, best_result)
        return best_result
