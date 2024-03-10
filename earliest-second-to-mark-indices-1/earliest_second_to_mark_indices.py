class Solution:
    def earliestSecondToMarkIndices(self, nums: list[int], changeIndices: list[int]) -> int:
        changeIndices = [n - 1 for n in changeIndices]
        
        wibble = [list() for i in range(len(nums))]
        for i, n in changeIndices:
            wibble[n].append(i)

        if sum([1 for l in wibble if len(l) == 0]):
            return -1
        
        return 0
