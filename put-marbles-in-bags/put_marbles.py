import math

class Solution:

    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        partitions = [weights[i] + weights[i+1] for i in range(0, len(weights)-1)]
        partitions.sort()
        required = k - 1
        
        maxSum = sum(partitions[0-required:])
        minSum = sum(partitions[:required])
        return maxSum - minSum

