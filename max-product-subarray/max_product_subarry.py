class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Highest negative, highest positive
        (bestValue, currentPositiveOnly, currentAbsolute) = (nums[0], nums[0], nums[0])
        for n in nums[1:]:
            if n > 0:
                currentPositiveOnly = currentPositiveOnly * n if currentPositiveOnly else n
                currentAbsolute = currentAbsolute * n if currentAbsolute else n
            elif n < 0:
                currentPositiveOnly = currentAbsolute * n if currentAbsolute < 0 else None
                currentAbsolute = currentAbsolute * n if currentAbsolute else n
            else:
                currentPositiveOnly = 0
                currentAbsolute = 0
            comparisonRange = [bestValue]
            if currentPositiveOnly != None:
                comparisonRange.append(currentPositiveOnly)
            if currentAbsolute:
                comparisonRange.append(currentAbsolute)
            bestValue = max(comparisonRange)

        # And again, but backwards!
        (currentPositiveOnly, currentAbsolute) = (nums[-1], nums[-1])
        for n in nums[-2::-1]:
            if n > 0:
                currentPositiveOnly = currentPositiveOnly * n if currentPositiveOnly else n
                currentAbsolute = currentAbsolute * n if currentAbsolute else n
            elif n < 0:
                currentPositiveOnly = currentAbsolute * n if currentAbsolute < 0 else None
                currentAbsolute = currentAbsolute * n if currentAbsolute else n
            else:
                currentPositiveOnly = 0
                currentAbsolute = 0
            comparisonRange = [bestValue]
            if currentPositiveOnly != None:
                comparisonRange.append(currentPositiveOnly)
            if currentAbsolute:
                comparisonRange.append(currentAbsolute)
            bestValue = max(comparisonRange)

        return bestValue
                
        