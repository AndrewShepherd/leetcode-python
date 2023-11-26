class Solution:
    def minimumSteps(self, s: str) -> int:
        target = 0
        swaps = 0
        for i,c in enumerate(s):
            if c == '0':
                swaps += i - target
                target += 1
        return swaps
        
