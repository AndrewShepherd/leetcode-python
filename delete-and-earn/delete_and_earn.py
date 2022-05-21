def solveForPairs(pairs, index, cache):
    if index >= len(pairs):
        return 0
    if (cache[index] != None):
        return cache[index]
    total = 0
    for i in range(index, len(pairs)):
        p = pairs[i]
        if (i == len(pairs)-1) or (pairs[i+1][0]-p[0] > 1):
            total += p[1]
        else:
            option1 = p[1] + solveForPairs(pairs, i+2, cache)
            option2 = solveForPairs(pairs, i+1, cache)
            result = total + max(option1, option2)
            cache[index] = result
            return result
    cache[index] = total
    return total

class Solution(object):
    def deleteAndEarn(self, nums):
        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1
        pairs = [(k, d[k] * k) for k in sorted(d.keys())]
        cache = [None] * len(pairs)
        return solveForPairs(pairs, 0, cache)
