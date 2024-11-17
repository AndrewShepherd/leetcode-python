

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        transformations = []
        for start, end in queries:
            transformations.append((start, -1))
            transformations.append((end + 1, 1))
        transformations.sort()
        t_index = 0
        t = 0
        for i,n in enumerate(nums):
            while(t_index < len(transformations) and transformations[t_index][0] == i):
                t += transformations[t_index][1]
                t_index += 1
            if n + t > 0:
                return False
        return True
