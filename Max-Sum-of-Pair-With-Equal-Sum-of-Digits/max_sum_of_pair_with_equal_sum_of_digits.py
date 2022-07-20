from collections import defaultdict
from optparse import Values

def binarySearch(target, nums, start, endExclusive):
    if (start >= endExclusive):
        return None
    tryIndex = (start + endExclusive) // 2
    if nums[tryIndex] < target:
        return binarySearch(target, nums, tryIndex + 1, endExclusive)
    elif nums[tryIndex] > target:
        return binarySearch(target, nums, start, endExclusive - 1)
    else:
        return (
            tryIndex,
            (tryIndex > 0 and nums[tryIndex-1] == target) or (tryIndex < len(nums)-1 and nums[tryIndex+1] == target)
        )
    return None

def sumOfDigits(n):
    s = 0
    while(n):
        s += n % 10
        n //= 10
    return s

class Solution:
    def maximumSum(self, nums) -> int:
        d = defaultdict(lambda: [-1, 0])
        for n in nums:
            s = sumOfDigits(n)
            d[s] = sorted(d[s] + [n])[1:]
        #result = -1
        max_result = -1
        for l,r in d.values():
            if l > 0 and r > 0:
                max_result = max(max_result, l + r)
        return max_result
