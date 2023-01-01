class Solution:
    def distinctPrimeFactors(self, nums) -> int:
        nums = set(nums)
        sieve = [False] * 1001
        count = 0
        for p in range(2, 1001):
            if not sieve[p]:
                for p2 in range(p*2, 1001, p):
                    sieve[p2] = True
                for n in nums:
                    if n % p == 0:
                        count += 1
                        break
        return count
