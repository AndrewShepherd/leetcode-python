def gcd(smaller, larger):
    if smaller > larger:
        smaller, larger = larger, smaller
    m = larger % smaller
    if m == 0:
        return smaller
    else:
        return gcd(m, smaller)



class Solution:
    def minOperations(self, nums, numsDivide) -> int:
        g = numsDivide[0]
        for i in range(1, len(numsDivide)):
            g = gcd(g, numsDivide[i])
        deletions = 0
        for n in sorted(nums):
            if g % n == 0:
                return deletions
            else:
                deletions += 1
        return -1