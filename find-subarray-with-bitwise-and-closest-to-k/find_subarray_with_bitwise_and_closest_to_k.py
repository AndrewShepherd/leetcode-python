from collections import defaultdict


def get_value(bit_counts):
    result = 0
    for k,v in bit_counts.items():
        if v:
            result |= k
    return result

def add_to(bit_counts, n):
    mask = 1 << 31
    while(mask):
        if mask & n:
            bit_counts[mask] += 1
        mask >>= 1

def remove_from(bit_counts, n):
    mask = 1 << 31
    while(mask):
        if mask & n:
            bit_counts[mask] -= 1
        mask >>= 1

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        bit_counts = defaultdict(lambda: 0)
        left = 0
        right = 0
        add_to(bit_counts, nums)
        best_result = abs(k-aggregate)
        
