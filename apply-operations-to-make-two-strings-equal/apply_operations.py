def solveRecursive(mismatches, x) -> int:
    if len(mismatches) == 0:
        return 0
    if len(mismatches) % 2:
        return -1
    distances = [(mismatches[i+1] - mismatches[i], i) for i in range(len(mismatches)-1)]
    distances.sort()

    available = [True] * len(mismatches)
    cost = 0  
    for d, i in distances:
        if available[i] and available[i+1]:
            this_cost = min(x, d)
            cost += this_cost
            available[i] = False
            available[i+1] = False
    
    mismatches = [m for m,a in zip(mismatches, available) if a]
    return cost + solveRecursive(mismatches, x)


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        mismatches = [i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]
        return solveRecursive(mismatches, x)

