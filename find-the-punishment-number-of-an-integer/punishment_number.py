def canBeParitioned(digits, start_index, target):
    i = start_index
    n = 0
    if start_index == len(digits):
        return target == 0
    while(start_index < len(digits)):
        n = n*10 + digits[start_index]
        if n > target:
            return False
        if canBeParitioned(digits, start_index + 1, target-n):
            return True
        start_index += 1
    return False

class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n+1):
            iSquared = i*i
            digits = [int(c) for c in str(iSquared)]
            if canBeParitioned(digits, 0, i):
                result += iSquared
        return result