segment_tree_depth = 18

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        if not nums:
            return 0
        segmentLists = [[0]*(2**i) for i in range(segment_tree_depth-1, -1, -1)]
        for n in nums:
            # Get the maximum value below n
            rangeStart,rangeEndExclusive = max(n-k, 0), n
            max_undervalue = 0
            for l in segmentLists:
                if rangeStart == rangeEndExclusive:
                    break
                if rangeStart % 2 != 0:
                    max_undervalue = max(max_undervalue, l[rangeStart])
                    rangeStart += 1
                if rangeEndExclusive % 2 != 0:
                    max_undervalue = max(max_undervalue, l[rangeEndExclusive-1])
                    rangeEndExclusive -= 1
                rangeStart //= 2
                rangeEndExclusive //= 2
            # Now set it if it's bigger than the existing
            new_value = max_undervalue + 1
            for l in segmentLists:
                if new_value > l[n]:
                    l[n] = new_value
                else:
                    break
                n //= 2

        return segmentLists[-1][0]