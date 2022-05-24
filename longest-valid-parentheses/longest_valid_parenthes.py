class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        best_so_far = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                amountToAdd = 2
                while(stack):
                    p = stack.pop()
                    if p > 0:
                        best_so_far = max(best_so_far, p)
                        amountToAdd += p
                    else:
                        if stack and stack[-1] > 0:
                            stack[-1] += amountToAdd
                        else:
                            stack.append(amountToAdd)
                        break
        return max(max(stack) if stack else 0, best_so_far)
        