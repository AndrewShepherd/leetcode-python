class Solution:
    def arrayChange(self, nums, operations):
        indexLookup = [None] * 1000001
        for i, n in enumerate(nums):
            indexLookup[n] = i
        for o, n in operations:
            lookedUpIndex = indexLookup[o]
            if (lookedUpIndex) == None:
                raise "How did that happen!"
            nums[indexLookup[o]] = n
            indexLookup[n] = lookedUpIndex
        return nums
        