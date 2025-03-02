from collections import Counter

def get_pairs(c):
    s = sum([k * v for k,v in c.items()])
    keys = c.keys()
    for k in keys:
        required_other = s - 2*k
        if required_other not in keys:
            continue
        if required_other == k and c[k] == 1:
            continue
        yield (k, required_other)

class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        c = Counter(nums)

        max_outlier = -1001
        for n1,n2 in get_pairs(c):
            max_outlier = max(max_outlier, n2)
        return max_outlier
