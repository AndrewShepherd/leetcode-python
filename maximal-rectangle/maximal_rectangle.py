class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        heights = [0] * len(matrix[0])
        max_value = 0
       
        for r in matrix:
            heights = [heights[i] + 1 if v == '1' else 0 for i, v in enumerate(r)]
            stack = []
            for i,this_height in enumerate(heights):
                while stack:
                    previous_height, previous_index = stack[-1]
                    if previous_height > this_height:
                        stack.pop()
                        max_value = max(max_value, (i-previous_index)*previous_height)
                    else:
                        break
                if (not stack) or (stack[-1][0] < this_height):
                    stack.append((this_height, i))
            for height,i in stack:
                max_value = max(max_value, (len(heights)-i)*height)
        return max_value
