class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeros = [0] * len(s)
        ones = [0] * len(s)
        for i,c in enumerate(s):
            l,o = (zeros, ones) if c == '0' else (ones, zeros)
            l[i] = 1 if i == 0 else l[i-1] + 1
            o[i] = 0 if i == 0 else o[i-1]
            

        # O(n^2) solution
        c = 0
        for i in range(len(zeros)):
            total_zeros = zeros[i]
            total_ones = ones[i]
            if (total_ones >= total_zeros * total_zeros):
                c += 1
            for j in range(0, i):
                if total_ones - ones[j] >= (total_zeros - zeros[j])**2:
                    c += 1                
        return c
        
