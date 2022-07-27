from collections import defaultdict, Counter
from functools import cache

modulus = 1000000007

def partitionCount(bagsToChooseFrom, requiredLength):
    if requiredLength == 0:
        return 1
    if requiredLength == 1:
        return bagsToChooseFrom
    if requiredLength == 2:
        return bagsToChooseFrom + (bagsToChooseFrom * (bagsToChooseFrom - 1)) // 2
    if bagsToChooseFrom == 1:
        return 1
    elif bagsToChooseFrom == 2:
        return requiredLength + 1
    else:
        return  partitionCount(bagsToChooseFrom, requiredLength - 1) + partitionCount(bagsToChooseFrom - 1, requiredLength)


def createFactorLookups(maxValue):
    result = [[1] for _ in range(maxValue+1)]
    for i in range(2, maxValue+1):
        for j in range(i, maxValue+1, i):
            result[j].append(i)
    return result

def getPrimes(maxValue):
    sieve = [False] * (maxValue + 1)
    for i in range(2, len(sieve)):
        if not(sieve[i]):
            yield i
        for j in range(i+i, len(sieve), i):
            sieve[j] = True


def gcd(smaller, larger):
    if smaller > larger:
        smaller, larger = larger, smaller
    if smaller == 1:
        return 1
    if smaller == 0:
        return larger
    if smaller == larger:
        return smaller
    return gcd(larger % smaller, smaller)

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
    numerator = 1
    denominator = 1
    for n, d in zip(multipliers, divisors):
        numerator *= n
        denominator *= d
        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g
    return numerator // denominator

@cache
def calculate_count(requiredLength, availableNumbers):
    return nChooseK(requiredLength + availableNumbers - 1, requiredLength)

def cacheResult(l):
    lookup = dict()
    def calculateUsingCache(n):
        if n not in lookup:
            lookup[n] = l(n)
        return lookup[n]
    return calculateUsingCache


# Sequence length is the number of distinct numbers
# eg [1 2 4 8 16 32]  has a sequence length of 6
def calculateWithOnePrimeFactor(sequence_length):
    # k is the required length of the ideal array
    return lambda k:calculate_count(k-1, sequence_length)

def calculateWithTwoPrimeFactorsOneToThePowerOfOne(theOtherPower):
    sequence_length = theOtherPower + 2
    @cache
    def calculate(k):
        return (sequence_length - 1) * calculate_count(k-1, sequence_length) - (sequence_length-2) * calculate_count(k-1, sequence_length - 1)
    return calculate

def calculateFor6(k):
    return calculateWithTwoPrimeFactorsOneToThePowerOfOne(1)
    #return 2 * calculate_count(k-1, 3) - calculate_count(k-1, 2)

# 2^2 * 3^1
def calculateFor12(k):
    return 3 * calculate_count(k-1, 4) -  2 * calculate_count(k-1, 3)

# 2^3 * 3^1
def calculateFor24(k):
    return 4 * calculate_count(k-1, 5) - 3 * calculate_count(k-1, 4)

# 2^4 * 3^1
def calculateFor48(k):
    return 5 * calculate_count(k-1, 6) - 4 * calculate_count(k-1, 5)

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


testPatternCounts = generatePatternCounts(10000)

def enumerateSubPatterns(pattern):
    if not pattern:
        yield pattern
    else:
        yield from enumerateSubPatterns(pattern[1:])
        for i in range(1, pattern[0] + 1):
            for subPattern in enumerateSubPatterns(pattern[1:]):
                yield (i,) + subPattern

def generatePatternCalculator(pattern, patternIndexes, patternCalculators):
    if pattern == tuple():
        return lambda required_length : 1
    if len(pattern) == 1:
        return calculateWithOnePrimeFactor(pattern[0]+1)

    if len(pattern) == 2 and pattern[0] == 1:
        return calculateWithTwoPrimeFactorsOneToThePowerOfOne(pattern[1])

    subPatterns = Counter([tuple(sorted(p)) for p in enumerateSubPatterns(pattern) if p != pattern])
    indexesAndMultipliers = [(patternIndexes[subPattern], subPatterns[subPattern]) for subPattern in subPatterns.keys()]

    dp = [1]

    #@cache
    def calculate(required_length):
        if required_length <= 1:
            return 1
        nonlocal dp
        if required_length < len(dp):
            return dp[required_length - 1]

        alreadyDone = len(dp)
        dp = dp + [None]*(required_length - alreadyDone)
        if len(dp) < required_length:
            raise Exception("Wrong")

#dp2[index] = sum([dp[f] for f in factorLookup[index]]) % modulus
        for k in range(alreadyDone+1, len(dp)+1):
            s = dp[k-2]
            s += sum([patternCalculators[i](k-1) * m for i,m in indexesAndMultipliers]) % modulus
            dp[k-1] = s % modulus
        if len(dp) < required_length:
            raise Exception("Wrong")
        return dp[required_length - 1]
    return calculate

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        patternCounts = generatePatternCounts(maxValue)
        patterns = patternCounts.keys()
        patternIndexes = dict()
        for i, v in enumerate(patterns):
            patternIndexes[v] = i

        patternCalculators = [None] * len(patterns)
        finalMultipliers = [0] * len(patterns)
        for i, v in enumerate(patterns):
            patternCalculators[i] = generatePatternCalculator(v, patternIndexes, patternCalculators)
            finalMultipliers[i] = patternCounts[v]

        dp = [c(n) for c in patternCalculators]

        finalSum = 0
        for z in zip(dp, finalMultipliers):
            finalSum += (z[0] * z[1]) % modulus
        return finalSum % modulus
        

        
        factorLookup = createFactorLookups(maxValue)

        calculators = [None] * (maxValue + 1)
        calculators[1] = lambda n:1
        for p in getPrimes(maxValue):
            exponent = 1
            p2 = p
            while p2 < len(calculators):
                calculators[p2] = calculateWithOnePrimeFactor(exponent + 1)
                p2 *= p
                exponent += 1
        dp = [0] + [1] * maxValue
        for _ in range(1, n):
            dp2 = dp[:]
            dp3 = [None] * len(dp)
            requiredLength = _ + 1
            
            for index in range(1, len(dp2)):
                dp2[index] = sum([dp[f] for f in factorLookup[index]]) % modulus
                if calculators[index]:
                    dp3[index] = calculators[index](requiredLength) % modulus
                if (dp3[index] != None) and (dp3[index] != dp2[index]):
                    requiredResult = dp2[index]
                    newResult = calculators[index](requiredLength)
                    raise Exception(f"Failed at index {index}. Required {requiredResult} but got {newResult}")
            dp = dp2
        return sum(dp) % modulus