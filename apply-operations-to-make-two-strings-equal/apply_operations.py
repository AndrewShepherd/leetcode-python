from functools import cache

call_count = 0

@cache
def solveRecursive(mismatches, x) -> int:
    global call_count
    call_count += 1
    if len(mismatches) == 0:
        return 0
    if len(mismatches) % 2:
        return -1
    if len(mismatches) == 2:
        return min(x, mismatches[1] - mismatches[0])
    return min(
        min(mismatches[1] - mismatches[0], x) + solveRecursive(mismatches[2:], x),
        min(mismatches[2] - mismatches[1], x) + solveRecursive((mismatches[0],) + mismatches[3:], x)
    )

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        global call_count
        call_count = 0
        mismatches = tuple(i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2)
        result = solveRecursive(mismatches, x)
        print(f'len(mismatches) = {len(mismatches)}, call_count = {call_count}')
        return result

