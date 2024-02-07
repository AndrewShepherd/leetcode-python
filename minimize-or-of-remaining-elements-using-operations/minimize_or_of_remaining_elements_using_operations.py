from collections import defaultdict

def dont_swap(state, n):
    swap_count, fixed, changeable = state
    next_fixed = fixed | changeable
    next_changeable = n & ~next_fixed
    return (swap_count, next_fixed, next_changeable)


def swap(state, n):
    swap_count, fixed, changeable = state
    next_changeable = changeable & n
    return (swap_count + 1, fixed, next_changeable) 


def get_override(s1, s2):
    s1,s2 = sorted([s1, s2])
    t1,f1,c1 = s1
    t2,f2,c2 = s2

    if (f1,c1) == (f2, c2):
        return (min(t1, t2), f1, c1)
    
    if f1&f2 == f1 and c1&c2 == c1:
        return s1
    
    if t1 == t2 and f1&f2 == f2 and c1&c2 == c2:
        return s2
    return None

def add_to_states(states, new_state):
    if new_state in states:
        return
    
    to_remove = []
    must_add = True
    for s in states:
        override = get_override(s, new_state)
        if override == None:
            continue
        elif override == s:
            must_add = False
            break
        else:
            to_remove.append(s)
    for s in to_remove:
        states.remove(s)
    if must_add:
        states.add(new_state)



class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        # Count each bit
        b = 1
        max_b = 1 << 30

        bit_counts = dict()
        while b < max_b:
            bit_counts[b] = sum([1 for n in nums if n & b])
            b <<= 1

        unmovable = 0
        for b in [b for b,c in bit_counts.items() if c > k]:
            unmovable |= b

        nums = [n & ~unmovable for n in nums]

        states = [(0, 0, nums[0])]
        for i in range(1, len(nums)):
            n = nums[i]
            next_states = set()
            for s in states:
                add_to_states(next_states, dont_swap(s, n))
                if s[0] < k:
                    add_to_states(next_states, swap(s, n))
            states = next_states

        return min([f | c | unmovable for s,f,c in states])
