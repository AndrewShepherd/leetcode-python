from math import log2, ceil

class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:

        powers_list = [0] * 32

        nums.sort()
        for l in [int(log2(n)) for n in nums]:
            powers_list[l] += 1

        

        bit = 1
        ops_count = 0 
        for i in range(len(powers_list)):
            if target & bit:
                powers_list[i] -= 1
            if powers_list[i] < 0:
                if i == len(powers_list) - 1:
                    return -1
                to_take = ceil((0 - powers_list[i])/2)
                powers_list[i+1] -= to_take
                ops_count += to_take
            if powers_list[i] >= 2 and i < len(powers_list) - 1:
                powers_list[i+1] += powers_list[i]//2
            bit <<= 1
        return ops_count
