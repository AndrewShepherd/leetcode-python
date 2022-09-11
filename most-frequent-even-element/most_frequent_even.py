from collections import Counter

class Solution:
    def mostFrequentEven(self, nums) -> int:
        c = Counter(n for n in nums if n%2==0)
        if not c:
            return -1
        else:
            items = list(c.items())
            items.sort(key = lambda i: (0-i[1], i[0]))
            return items[0][0]
