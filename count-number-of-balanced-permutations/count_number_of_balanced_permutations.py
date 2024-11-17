from collections import Counter
from math import comb
from functools import cache

modulo = 10**9 + 7
ORD_0 = ord('0')


def combinations(l):
    if len(l) == 0:
        return 1
    if len(l) == 1:
        return 1
    t = sum(l)
    r = comb(t, l[0]) % modulo
    if len(l) > 2:
        r = r * combinations(l[1:]) % modulo
    return r

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        num = [ord(n) - ORD_0 for n in num]
        s = sum(num)
        if (s%2):
            return 0
        c = Counter(num)
        
        c_array = sorted(list(c.items()))
        larger_bucket_size = len(num)//2 + len(num)%2

        @cache
        def sum_available_counts(start_index):
            return sum([c_array[i][1] for i in range(start_index, len(c_array))])

        @cache 
        def get_permutations(start_index, target_count, target_sum):
            if target_count == 0:
                if target_sum == 0:
                    return combinations([e[1] for e in c_array[start_index:]])
                else:
                    return 0

            if start_index == len(c_array):
                return 0
            if target_sum < 0:
                return 0
            
            v, c = c_array[start_index]
            
            if v*target_count > target_sum:
                # We already know there is no solution from here
                return 0
            
            count_remaining = sum_available_counts(start_index)
            if count_remaining < target_count:
                return 0
            
            other_count = count_remaining - target_count
            result = 0
            for trial_count in range(0, c+1):
                if target_sum < v * trial_count:
                    break
                sub_permutations = get_permutations(start_index + 1, target_count - trial_count, target_sum - v * trial_count)
                if sub_permutations != 0:
                    other_tokens = c - trial_count                    
                    this_comb = comb(target_count, trial_count) % modulo
                    other_comb = comb(other_count, other_tokens) % modulo
                    this_result = (sub_permutations * this_comb * other_comb) % modulo
                    result = (result + this_result) % modulo
            return result

        return get_permutations(0, larger_bucket_size, s//2)

