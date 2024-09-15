class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        start.sort()
        total_range = start[-1] - start[0] + d
        max_possible_result = total_range // (len(start)-1)
        best_so_far = 0
        while(max_possible_result > best_so_far):
            interval = (max_possible_result + best_so_far) // 2 + 1
            last_value = start[0]
            failed = False
            for i in range(1, len(start)):
                target_value = last_value + interval
                if target_value < start[i]:
                    target_value = start[i]
                elif target_value > start[i] + d:
                    target_value = start[i] + d
                if target_value - last_value < interval:
                    failed = True
                    break
                last_value = target_value
            if not(failed):
                best_so_far = interval
            else:
                max_possible_result = interval - 1
        return best_so_far