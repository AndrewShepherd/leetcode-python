from collections import Counter

class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        c = Counter(derived)
        return c[1] % 2 == 0


