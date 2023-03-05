from collections import defaultdict
from math import sqrt


class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        primes = []
        sieve = [False] * int(sqrt(max(nums)) + 1)
        for n in range(2, len(sieve)):
            if not sieve[n]:
                primes.append(n)
                for j in range(n*2, len(sieve), n):
                    sieve[j] = True

        def get_prime_factors(n): 
            result = set()
            for p in primes:
                while n%p == 0:
                    result.add(p)
                    n //= p
                if n == 1:
                    break
            if n > 1:
                result.add(n)
            return result
        
        max_index_of_factors = dict()
        
        factor_sets = [None] * len(nums)
        for i,n in enumerate(nums):
            s = get_prime_factors(n)
            factor_sets[i] = s
            for p in s:
                max_index_of_factors[p] = i

        min_split = 0
        checked_index = -1
        while(checked_index < min_split):
            checked_index += 1
            f = factor_sets[checked_index]
            for p in f:
                min_split = max(min_split, max_index_of_factors[p])
            if min_split == len(nums) - 1:
                return -1
        return min_split
