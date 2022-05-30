# copied from https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2086820/Python-3-Monotonic-stack-O(N)-solution


class Solution:
    def totalSteps(self, nums):
        stack=[]
        maxx=0
        for i in nums:
            count=1
            while stack!=[] and stack[-1][0] <= i:
                v=stack.pop()
                count=max(count,v[1]+1)
            if stack==[]:
                count=0
            maxx=max(maxx,count)
            stack.append([i,count])
        return maxx