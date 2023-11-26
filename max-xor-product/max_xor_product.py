modulo = 1000000007

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if n == 0:
            return (a * b) % modulo

        m = (1 << n) - 1
        left_value = a & (~m)
        right_value = b & (~m)

        bit_mask = 1 << (n-1)
        while bit_mask:
            if (a & bit_mask) == (b & bit_mask):
                left_value += bit_mask
                right_value += bit_mask
            elif (left_value < right_value):
                left_value += bit_mask
            else:
                right_value += bit_mask
            bit_mask >>= 1
        return ((left_value % modulo) * (right_value % modulo)) % modulo 
