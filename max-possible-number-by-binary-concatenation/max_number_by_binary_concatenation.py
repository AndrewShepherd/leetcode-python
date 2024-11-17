from functools import reduce

def get_bitlength(n):
    if n == 0:
        return 1
    result = 0
    while(n):
        n >>= 1
        result += 1
    return result

def concatenate(left, right):
    left_number = left.value if isinstance(left, number_wrapper) else left
    right_wrapper = right if isinstance(right, number_wrapper) else number_wrapper(right)
    return left_number << right_wrapper.bit_length | right_wrapper.value

class number_wrapper:
    def __init__(self, n):
        self.value = n
        self.bit_length = get_bitlength(n)
    
    # returns true if self should go first
    # returns false if other should go first
    def __lt__(self, other):
        return concatenate(self, other) > concatenate(other, self)

class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        return reduce(
            concatenate,
            sorted(map(number_wrapper, nums)), 
            0
        )
