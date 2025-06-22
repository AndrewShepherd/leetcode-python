from functools import cache

@cache
def waysToSolve(target: int, availableValues: tuple[int]) -> int:
    if target == 0:
        return 1
    if (len(availableValues) == 0):
        return 0
    last_value = availableValues[len(availableValues) - 1]
    result = 0
    m = 0
    while m * last_value <= target:
        result += waysToSolve(target - m * last_value, availableValues[:-1]) 
        m += 1
    return result

class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        result = []
        dp = []
        availableValues = tuple()
        for i,n in enumerate(numWays):
            target = i + 1
            expected_result = waysToSolve(target, availableValues)
            if (n < expected_result):
                return []
            elif (n == expected_result):
                continue
            elif (n == expected_result + 1):
                availableValues = (*availableValues, target)
            else:
                return []
        return list(availableValues)
