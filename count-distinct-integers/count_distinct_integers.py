class Solution:
    def countDistinctIntegers(self, nums) -> int:
        encountered = set()
        for n in nums:
            encountered.add(n)
            r = int(str(n)[::-1])
            encountered.add(r)
        return len(encountered)
