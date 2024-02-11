all_bits = 0xFFFFFFFF

def iterate_through_bits():
    less_significant_bits = all_bits
    b = 1 << 31
    while(b):
        less_significant_bits &= ~b
        yield b,less_significant_bits
        b >>= 1

class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        bits_we_cant_remove = 0
        for b, less_significant_bits in iterate_through_bits():
            unswapped_count = 0
            bits_not_cancelled = all_bits
            irrelevant_bits = bits_we_cant_remove | less_significant_bits
            for n in nums:
                bits_not_cancelled = bits_not_cancelled & n
                if (bits_not_cancelled | irrelevant_bits) == irrelevant_bits:
                    unswapped_count += 1
                    bits_not_cancelled = all_bits
            swaps_required = len(nums) - unswapped_count
            if (swaps_required > k):
                bits_we_cant_remove |= b
        return bits_we_cant_remove