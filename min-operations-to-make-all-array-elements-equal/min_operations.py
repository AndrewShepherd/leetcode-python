import bisect

# problem 2602

def solve_single_query(nums, q):
    return sum([abs(n-q) for n in nums])

def solve_slowly(nums, queries):
    return [solve_single_query(nums, q) for q in queries]


class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        # return solve_slowly(nums, queries)
        nums.sort()
        going_up = [0] * len(nums)
        for i in range(1, len(nums)):
            going_up[i] = going_up[i-1] + (nums[i] - nums[i-1]) * i

        going_down = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            going_down[i] = going_down[i+1] + (nums[i+1] - nums[i]) * (len(nums)-1-i)
        
        result = []
        for q in queries:
            index = bisect.bisect_left(nums, q)
            b_index = bisect.bisect(nums, q)
            if 0 <= index < len(nums) and nums[index] == q:
                result.append(going_up[index] + going_down[index])
            elif index >= len(nums):
                result.append(going_up[-1] + (q - nums[-1]) * len(nums))
            elif index == 0 and q < nums[0]:
                #brute_force = sum([abs(n-q) for n in nums])
                calculated = going_down[0] + (nums[0]-q) * len(nums)
                result.append(calculated)
            else:
                from_below = (q - nums[index-1]) * index + going_up[index - 1]
                count_of_numbers_above = len(nums)-index
                from_above = (nums[index]-q) * count_of_numbers_above + going_down[index]
                value = from_below + from_above 
                result.append(value)

        return result
        
        
