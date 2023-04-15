class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = 0
        ones = 0
        best_result = 0
        for c in s:
            if c == '0':
                if ones:
                    zeros = 1
                    ones = 0
                else:
                    zeros += 1
            if c == '1':
                ones += 1
                best_result = max(best_result, min(ones, zeros)*2)
        return best_result
        
