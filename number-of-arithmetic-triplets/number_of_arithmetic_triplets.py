class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        matches = [False] * 350
        for n in nums:
            matches[n] = True
        count = 0
        for n in nums:
            if matches[n] and matches[n+diff] and matches[n+diff*2]:
                count += 1
        return count