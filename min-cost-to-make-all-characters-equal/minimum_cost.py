import math

class Solution:
    def minimumCost(self, s: str) -> int:
        f0 = [None] * len(s)
        f1 = [None] * len(s)
        b0 = [None] * len(s)
        b1 = [None] * len(s)
        
        f0[0] = 0 if s[0] == '0' else 1
        f1[0] = 0 if s[0] == '1' else 1

        for i in range(1, len(s)):
            if s[i] == '0':
                f0[i] = f0[i-1]
                f1[i] = f0[i-1] + (i+1)
            else:
                f0[i] = f1[i-1] + i + 1
                f1[i] = f1[i-1]

        b0[-1] = 0 if s[-1] == '0' else 1
        b1[-1] = 0 if s[-1] == '1' else 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                b0[i] = b0[i+1]
                b1[i] = b0[i+1] + len(s) - i
            else:
                b0[i] = b1[i+1] + len(s) - i
                b1[i] = b1[i+1]  
        min_result = math.inf

        for i in range(len(s)):
            # If I make it zero
            if i == 0:
                zeros = b0[0]
                ones = b1[0]
            else: 
                zeros = min(b0[i] + f0[i-1], b0[i-1] + f0[i])
                ones = min(b1[i] + f1[i-1], b1[i-1] + f1[i])
            min_result = min([min_result, zeros, ones])
        return min_result
