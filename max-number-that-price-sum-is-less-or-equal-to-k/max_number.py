def count_where_bit_is_set(n, x):
    mask = 1 << (x-1)
    result = 0
    if n & mask:
        result += n % (mask) + 1    
    n2 = n - (n % (mask << 1))
    result += n2 // 2
    return result

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:        
        def calculate_price_up_to_and_including(n):
            bit = x
            price = 0
            while(n >= 1<<(bit-1)):
                price += count_where_bit_is_set(n, bit)
                bit += x
            return price

        left = 0
        right = k * (2**(x-1)) + 1
        while(right - left > 1):
            mid_point = (left + right)//2
            price = calculate_price_up_to_and_including(mid_point)
            if price > k:
                right = mid_point - 1
            else:
                left = mid_point

        if calculate_price_up_to_and_including(right) <= k:
            return right
        else:
            return left
        
