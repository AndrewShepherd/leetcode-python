class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_volume = 0
        while right > left:
            max_volume = max(
                max_volume, 
                min(
                    height[right],
                    height[left]
                )*(right-left)
            )
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_volume