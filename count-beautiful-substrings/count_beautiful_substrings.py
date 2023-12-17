from collections import defaultdict, Counter
from math import ceil, sqrt


def factorize(n):
    sieve_size = ceil(sqrt(n)) + 1
    sieve = [True] * sieve_size
    result = []
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i*2, len(sieve), i):
                sieve[j] = False
            while (n%i) == 0:
                result.append(i)
                n //= i
            if n == 1:
                break
    if n != 1:
        result.append(n)
    return result

def get_required_square_root(k) -> int:
    factors = factorize(k)
    factor_counts = Counter(factors)
    required = 1
    for f,c in factor_counts.items():
        required *= (f**(ceil(c/2)))
    return required


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        required = get_required_square_root(k)

        vowel_counts = 0
        consonant_counts = 0

        zipped = [None] * len(s)
        for i,c in enumerate(s):
            is_vowel = c in {'a','e','i','o','u'}
            if is_vowel:
                vowel_counts += 1
            else:
                consonant_counts += 1
            
            delta = vowel_counts - consonant_counts
            zipped[i] = (delta, vowel_counts % required)

        counts = Counter(zipped)
        counts[(0, 0)] += 1

        result = 0
        for v in reversed(zipped):
            counts[v] -= 1
            result += counts[v]
        return result                
