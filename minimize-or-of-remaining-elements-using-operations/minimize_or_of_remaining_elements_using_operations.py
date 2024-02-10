bit_count = 30
all_bits = (1 << bit_count) - 1


def bits_to_right_of(bit):
    return (1 << bit) - 1

class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        # this will contain the 'or' of all final elements of array
        ans = 0
        # Iterating from Most Significant Bit to Least Significant Bit
        for bit in range(bit_count - 1, -1, -1):
            # target: represents the set of bits we are not concerned with for this iteration
            target = (ans | bits_to_right_of(bit))
            elements_that_dont_need_to_be_swapped = 0 
            # cur: The set of bits that will NOT be cancelled out, 
            #      given whether the current element is swapping with the previous element 
            #      or not
            cur = all_bits
            for num in nums:
                cur &= num
                if cur | target == target:  # There is nothing in this group we care about
                    elements_that_dont_need_to_be_swapped += 1
                    cur = all_bits
            # we have to keep the current bit if (len(nums)-count) is greater than k 
            # otherwise we can remove current bit in less than or equal to k operations
            swaps_required = len(nums) - elements_that_dont_need_to_be_swapped
            if swaps_required> k:
                ans |= (1 << bit)
        return ans