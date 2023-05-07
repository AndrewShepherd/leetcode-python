from collections import Counter
import math


def generate_primes(up_to):
    sieve = [False] * (up_to+1)
    for i in range(2, len(sieve)):
        if not sieve[i]:
            yield i
            for j in range(i*2, len(sieve), i):
                sieve[j] = True

def factorize(n, primes):
    l = []
    for p in primes:
        while n % p == 0:
            l.append(p)
            n //= p
        if n == 1:
            break
    return Counter(l)

def gcd(bigger, smaller):
    if bigger < smaller:
        bigger,smaller = smaller,bigger
    if bigger == smaller:
        return bigger
    if smaller == 1:
        return 1
    diff = bigger - smaller
    return gcd(diff, smaller)


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        s = set([tuple(nums)])
        transformations = -1
        while(s):
            transformations += 1
            set2 = set()
            for nList in s:
                c = Counter(nList)
                if c[1]:
                    return transformations + sum([1 for n in nList if n != 1])
                for i in range(1, len(nList)):
                    if nList[i] != nList[i-1]:
                        g = gcd(nList[i], nList[i-1])
                        if nList[i-1] != g:
                            new_tuple = nList[:i-1] + (g,) + nList[i:]
                            set2.add(new_tuple)
                        if nList[i] != g:
                            new_tuple = nList[:i] + (g,) + nList[i+1:]
                            set2.add(new_tuple)
            s = set2

        return -1