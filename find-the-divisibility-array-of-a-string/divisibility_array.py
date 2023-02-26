class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        result = [0] * len(word)
        
        t = 0
        for i,c in enumerate(word):
            t = t * 10 + int(c)
            if t % m == 0:
                result[i] = 1
            while t >= m:
                t -= m
        return result
        
