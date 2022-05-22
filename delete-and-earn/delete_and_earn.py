class Solution(object):
    def deleteAndEarn(self, nums):

        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1
        pairs = [(k, d[k] * k) for k in sorted(d.keys())]

        results = [None] * len(pairs)
        for i, p in enumerate(pairs):
            if i == 0:
                results[i] = p[1]
            elif p[0] - pairs[i-1][0] > 1:
                results[i] = results[i-1] + p[1]
            else:
                results[i] = max(
                    p[1] + (results[i-2] if i > 1 else 0),
                    results[i-1]
                )
        return max(results[-2:])