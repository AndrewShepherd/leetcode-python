class Solution:
    def longestNiceSubarray(self, nums) -> int:
        bits = [-1] * 30
        max_start_index=0
        longest_length = 0
        for i,n in enumerate(nums):
            bit_index = -1
            while(n):
                bit_index += 1
                if n&1:
                    if(bits[bit_index] < max_start_index):
                        bits[bit_index] = i
                    else:
                        max_start_index = bits[bit_index] + 1
                        bits[bit_index] = i
                n = n//2
            longest_length = max(i-max_start_index+1, longest_length)
        return longest_length