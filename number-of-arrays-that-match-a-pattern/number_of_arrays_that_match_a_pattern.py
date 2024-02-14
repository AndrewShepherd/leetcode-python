def convert_difference(d):
    if d > 0:
        return 'z'
    elif d < 0:
        return 'y'
    else:
        return 'v'
    
def create_lookup(p):
    p_lookup = [0] * len(p)
    matching_prefix_length = 0
    j = 1
    for j in range(1, len(p)):
        if p[matching_prefix_length] == p[j]:
            matching_prefix_length += 1
        else:
            while True :
                if (matching_prefix_length == 0):
                    break
                if p[:matching_prefix_length] == p[j-matching_prefix_length+1:j+1]:
                    break
                matching_prefix_length -= 1
        p_lookup[j] = matching_prefix_length
    return p_lookup

def dumb_search(p, n):
    index = 0
    while True:
        index = n.find(p, index)
        if (index == -1):
            break
        yield index
        index += 1

def smart_search(p, n):
    p_lookup = create_lookup(p)
    n_index = 0
    p_index = 0
    while n_index != len(n):
        if p[p_index] == n[n_index]:
            if p_index == len(p) - 1:
                yield n_index - len(p) + 1
                p_index = p_lookup[p_index]
                n_index += 1
            else:
                p_index += 1
                n_index += 1
        else:
            if p_index > 0:
                p_index = p_lookup[p_index-1]
            else:
                n_index += 1

def count_matches(p, n):
    c = 0
    for v in smart_search(p, n):
        c += 1
    return c

class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        nums_as_pattern = [convert_difference(nums[i] - nums[i-1]) for i in range(1, len(nums))]
        pattern = [convert_difference(e) for e in pattern]        
        return count_matches(''.join(pattern), ''.join(nums_as_pattern))

            
        
