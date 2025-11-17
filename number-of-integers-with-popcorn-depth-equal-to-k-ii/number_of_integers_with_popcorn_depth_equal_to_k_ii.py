from functools import cache
max_pd = 4


def bit_count(n):
    m = 1
    c = 0
    while m <= n:
        c += 1 if (m&n) else 0
        m <<= 1
    return c


@cache 
def pd(n):
    if (n == 1):
        return 0
    bc = bit_count(n)
    return 1 + pd(bc)

def zeros():
    return [0] * (max_pd + 1)

def as_array(n):
    a = zeros()
    a[n] = 1
    return a



def combine(l1, l2):
    return [v1 + v2 for v1,v2 in zip(l1, l2)]

def lsb(n):
    return n & (-n)



class Solution:
    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        result = []
        nums = [pd(n) for n in nums]
        depths = [as_array(n) for n in nums]

        fenwick = [zeros() for n in range(len(nums))]

        def mutate(index, mutate_action):
            one_based_index = index + 1
            while(one_based_index -1 < len(fenwick)):
                mutate_action(fenwick[one_based_index - 1])
                one_based_index += lsb(one_based_index)

        def get_prefix_sum(inclusive_index, bit_count):
            if (inclusive_index < 0):
                return 0
            one_based_index = inclusive_index + 1
            aggregate = fenwick[one_based_index-1][bit_count]
            while(True):
                one_based_index -= lsb(one_based_index)
                if one_based_index == 0:
                    break
                aggregate += fenwick[one_based_index - 1][bit_count]
            return aggregate

        for i,n in enumerate(nums):
            def m(a):
                a[n] = a[n] + 1
            mutate(i, m)

        def get_value(arrays_index, range_start, range_end_exclusive, matching_value):

            if (matching_value > max_pd):
                return 0

            total_value = 0
            subtract_value = 0

            total_index_one_based = range_end_exclusive
            subtract_index_one_based = range_start

            while(total_index_one_based != subtract_index_one_based):
                if total_index_one_based > subtract_index_one_based:
                    total_value += fenwick[total_index_one_based - 1][matching_value]
                    total_index_one_based -= lsb(total_index_one_based)
                else:
                    subtract_value += fenwick[subtract_index_one_based - 1][matching_value]
                    subtract_index_one_based -= lsb(subtract_index_one_based)
            return total_value - subtract_value
        
        def change(array, dec_index, inc_index):
            array[inc_index] += 1
            array[dec_index] -= 1

        for (q, *p) in queries:
            if q == 1:
                l,r,k = p
                result.append(get_value(0, l, r+1, k))
            elif q == 2:
                idx, val = p
                original_value = nums[idx]
                new_value = pd(val)
                if new_value == original_value:
                    continue
                nums[idx] = new_value

                mutate(idx, lambda a: change(a, original_value, new_value))

        
        return result
