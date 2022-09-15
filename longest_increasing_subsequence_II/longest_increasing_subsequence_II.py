import math

segment_tree_depth = 18

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        if not nums:
            return 0
        segmentTrees = [[0]*(2**i) for i in range(segment_tree_depth)]
        for n in nums:
            # Get the maximum value below n
            rangeStart,rangeEndExclusive = max(n-k, 0), n
            max_undervalue = 0
            for l in reversed(segmentTrees):
                if rangeStart == rangeEndExclusive:
                    break
                if rangeStart & 1:
                    max_undervalue = max(max_undervalue, l[rangeStart])
                    rangeStart += 1
                if rangeEndExclusive & 1:
                    max_undervalue = max(max_undervalue, l[rangeEndExclusive-1])
                    rangeEndExclusive -= 1
                rangeStart //= 2
                rangeEndExclusive //= 2
            # Now set it if it's bigger than the existing
            new_value = max_undervalue + 1
            for l in reversed(segmentTrees):
                if new_value > l[n]:
                    l[n] = new_value
                else:
                    break
                n //= 2

        return segmentTrees[0][0]