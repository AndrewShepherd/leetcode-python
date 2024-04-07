import math

class Solution:
    def minOperations(self, k: int) -> int:
        n = 1
        if k == 1:
            return 0
        
        def result_with_just_duplications(n):
            return math.ceil((k-n)/n) + n-1
        
        best_result = k
        while(n < k):
            best_result = min(best_result, result_with_just_duplications(n))
            n = n+1
        return best_result
