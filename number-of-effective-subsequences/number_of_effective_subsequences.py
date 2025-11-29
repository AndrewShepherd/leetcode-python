from collections import defaultdict

MODULO = 10**9 + 7

def get_all_combinations(combination_length, not_exceeding):
    if combination_length <= not_exceeding:
        if (combination_length == 1):
            for i in range(0, not_exceeding):
                yield [i]
        else:
            for sub_array in get_all_combinations(combination_length - 1, not_exceeding - 1):
                yield sub_array + [not_exceeding - 1]
            for sub_array in get_all_combinations(combination_length, not_exceeding - 1):
                yield sub_array



class Solution:
    def countEffective(self, nums: list[int]) -> int:
        d = defaultdict(set)
        for i,n in enumerate(nums):
            f = 1
            while(n):
                if n & f:
                    d[f].add(i)
                    n -= f
                f <<= 1

        result = 0
        
        keys = list(d.keys())

        for i,k in enumerate(keys):
            result = result + pow(2, len(nums) - len(d[k]), MODULO)
            for j in range(1, i+1):
                union_lengths = []
                for combination in get_all_combinations(j, i):
                    u = d[k]
                    for entry in combination:
                        entry_key = keys[entry]
                        u = u.union(d[entry_key])
                    union_lengths.append(len(u))
                deltas = [pow(2, len(nums) - u, MODULO) for u in union_lengths]
                delta_sum = sum(deltas) % MODULO
                if j % 2:
                    result = (result - delta_sum) % MODULO
                else:
                    result = (result + delta_sum) % MODULO

        return result
