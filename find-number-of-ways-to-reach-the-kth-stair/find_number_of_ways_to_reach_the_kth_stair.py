from functools import cache

state_count = 0

class Solution:
    def waysToReachStair(self, k: int) -> int:
        # state = (current_stair, jump, has_just_gone_down)
        global state_count
        state_count = 0

        @cache
        def number_of_ways(current_start, jump, has_just_gone_down):
            global state_count
            state_count += 1
            if current_start > k + 1:
                return 0
            result = 0
            if current_start == k:
                result += 1
            if current_start > 0 and not has_just_gone_down:
                result += number_of_ways(current_start - 1, jump, True)
            result += number_of_ways(current_start + 2**jump, jump+1, False)
            return result
        result = number_of_ways(1, 0, False)
        print(f'k = {k}, state_count = {state_count}')
        return result
