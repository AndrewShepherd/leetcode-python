from collections import Counter
from math import comb
from functools import cache, reduce



def get_permutation_count(l, stop_at):
    accumulation = 1
    accumuated_length = 0
    for _,n in l:
        accumulation *= comb(accumuated_length + n, n)
        accumuated_length += n
        if (accumulation >= stop_at):
            return stop_at
    return accumulation

def take_at(l, index):
    c,n = l[index]
    if n == 1:
        return (c, l[:index] + l[index+1:])
    else:
        return (c, l[:index] + [(c, n-1)] + l[index+1:])
    
def solve(l, k):
    index_to_try = 0
    s = ''
    while (l):
        c,l_new = take_at(l, index_to_try)
        l_new_permutations = get_permutation_count(l_new, k)
        if (l_new_permutations >= k):
            s += c
            l = l_new
            index_to_try = 0
        else:
            k -= l_new_permutations
            index_to_try += 1
    return s


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        c = Counter(s)
        l = sorted(c.items())
        middle_char = None
        for c, v  in l:
            if v % 2 == 1:
                middle_char = c

        l = [(c, v//2) for c,v in l if v > 1]

        permutation_count = get_permutation_count(l, k)
        if permutation_count < k:
            return ''

        result = solve(l, k)
        if (middle_char == None):
            return result + result[::-1]
        else:
            return result + middle_char + result[::-1]
