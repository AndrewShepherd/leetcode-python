def get_factors(n):
    return [f for f in range(1, n+1) if n%f == 0]

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        factors = get_factors(n)
        for f in factors:
            w = sorted(s[:f])
            failed = False
            for i in range(f, len(s), f):
                if sorted(s[i:i+f]) != w:
                    failed = True
                    break
            if not failed:
                return f