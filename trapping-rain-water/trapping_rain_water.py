from itertools import accumulate

class Solution(object):
    def trap(self, height):

        maxLeft = tuple(accumulate(height, max))
        maxRight = tuple(accumulate(reversed(height), max))[::-1]

        total = 0
        for i in range(1,len(height)-1):
            total += max(
                min(maxLeft[i-1], maxRight[i+1]) - height[i],
                0
            )
        return total
