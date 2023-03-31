
class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        primes = []
        sieve = [True] * 1000
        for i in range(2, len(sieve)):
            if sieve[i]:
                primes.append(i)
                for j in range(i+i, len(sieve), i):
                    sieve[j] = False
        last = 0
        for n in nums:
            if n <= last:
                return False
            smallest = n
            for p in primes:
                if p >= n:
                    break
                if n - p > last:
                    smallest = n - p
            if smallest < last:
                return False
            last = smallest
        return True
