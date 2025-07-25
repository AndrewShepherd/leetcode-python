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



def as_array(n):
    a = [0] * (max_pd + 1)
    a[n] = 1
    return a



def combine(l1, l2):
    return [v1 + v2 for v1,v2 in zip(l1, l2)]



class Solution:
    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        result = []
        depths = [as_array(pd(n)) for n in nums]
        #print(f'original: {depths}')
        arrays = [depths]
        while(len(arrays[-1]) > 1):
            source_array = arrays[-1]
            new_array = [
                combine(
                    source_array[i], 
                    source_array[i+1]
                ) if i < len(source_array)-1 
                else source_array[i][:]
                for i in range(0, len(source_array), 2)
            ]            
            arrays.append(new_array)

        def get_value(arrays_index, range_start, range_end_exclusive, matching_value):
            if matching_value > max_pd:
                return 0
            if range_end_exclusive - range_start <= 0:
                return 0
            elif range_end_exclusive - range_start == 1:
                return arrays[arrays_index][range_start][matching_value]
            else:
                result = 0
                if range_start % 2 == 1:
                    result += arrays[arrays_index][range_start][matching_value]
                    range_start += 1
                if range_end_exclusive % 2 == 1:
                    result += arrays[arrays_index][range_end_exclusive-1][matching_value]
                return result + get_value(arrays_index + 1, range_start // 2, range_end_exclusive//2, matching_value)
        
        
        def mutate(arrays_index, index, mutate_action):
            if arrays_index >= len(arrays):
                return
            this_array = arrays[arrays_index][index]
            mutate_action(this_array)
            mutate(arrays_index + 1, index // 2, mutate_action)


        def change(array, dec_index, inc_index):
            array[inc_index] += 1
            array[dec_index] -= 1

        for (q, *p) in queries:
            if q == 1:
                l,r,k = p
                result.append(get_value(0, l, r+1, k))
            elif q == 2:
                idx, val = p
                original_value = None
                for i,n in enumerate(arrays[0][idx]):
                    if n:
                        original_value = i
                        break
                new_value = pd(val)
                if new_value == original_value:
                    continue

                mutate(0, idx, lambda a: change(a, original_value, new_value))

        
        return result
