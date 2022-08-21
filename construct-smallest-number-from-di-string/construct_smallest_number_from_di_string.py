def translate(l):
    return "".join([chr(ord('1')+n) for n in l])

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        usedValues = [False] * 9

        def solveRecursively(lastIndex, patternIndex):
            if patternIndex == len(pattern):
                return True, []
            if pattern[patternIndex] == 'I':
                for i in range(lastIndex+1, len(usedValues)):
                    if not usedValues[i]:
                        usedValues[i] = True
                        success, result = solveRecursively(i, patternIndex + 1)
                        if success:
                            return True, [i] + result
                        usedValues[i] = False
                return False, []
            else:
                for i in range(lastIndex):
                    if not usedValues[i]:
                        usedValues[i] = True
                        success, result = solveRecursively(i, patternIndex + 1)
                        if success:
                            return True, [i] + result
                        usedValues[i] = False
                return False, []

        for i in range(len(usedValues)):
            usedValues[i] = True
            success, result = solveRecursively(i, 0)
            if(success):
                return translate([i] + result)
            usedValues[i] = False
        return None