from collections import defaultdict, Counter
from functools import cache
import math

# See https://leetcode.com/submissions/detail/760266018/

modulus = 1000000007

######################################
# This section is about implementing
# nChooseK
def subtractRange(r:range, s:range):
    if s.start <= r.start:
        start = s.stop
    else:
        start = r.start
    if r.stop <= s.stop:
        stop = s.start
    else:
        stop = r.stop
    return range(start, stop)

def removeRangeOverlaps(r1:range, r2:range):
    if r1.start >= r2.stop:
        return r1, r2
    if r2.start >= r1.stop:
        return r1, r2
    overlap = range(max(r1.start, r2.start), min(r1.stop, r2.stop))
    return subtractRange(r1, overlap), subtractRange(r2, overlap)
    
# I have a stack of n cards, I can choose k of them
@cache
def nChooseK(n, k):
    # (n!)/(n-k)!(k)!
    multipliers = range(max(n-k+1, 1), n+1)
    divisors = range(1, k+1)

    multipliers, divisors = removeRangeOverlaps(multipliers, divisors)
    return math.prod(multipliers)//math.prod(divisors)


###########################################################
# These three methods are about generating the patterns
#
def getPrimes(maxValue):
    sieve = [False] * (maxValue + 1)
    for i in range(2, len(sieve)):
        if not(sieve[i]):
            yield i
        for j in range(i+i, len(sieve), i):
            sieve[j] = True

def enumerateAllPatterns(primes, upToPrimeIndex, numberRemaining):
    if upToPrimeIndex > 0:
        for i in range(upToPrimeIndex):
            p = primes[i]
            if p > numberRemaining:
                break
            exp = 1
            while p**exp <= numberRemaining:
                yield (exp,)
                for pattern in enumerateAllPatterns(primes, i, numberRemaining//(p**exp)):
                    yield pattern + (exp,)
                exp += 1

def generatePatternCounts(maxValue):
    primes = list(getPrimes(maxValue))
    d = defaultdict(lambda:0)
    c = 0
    for p in enumerateAllPatterns(primes, len(primes), maxValue):
        s = tuple(sorted(p))
        d[s] = d[s] + 1
        c += 1
    d[tuple()] = 1
    return d


def performTheCalculation(pattern, required_length):
    return math.prod(nChooseK(required_length + ct - 1, ct) for ct in pattern)

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        patternCounts = generatePatternCounts(maxValue)
        finalSum = 0
        for pattern, count in patternCounts.items():
            finalSum = (finalSum + performTheCalculation(pattern, n) * count) % modulus
        return finalSum

