def getBitIndexes(n):
    i = 0
    oneIndexes = []
    zeroIndexes = []
    while(n):
        if n&1:
            oneIndexes.append(i)
        else:
            zeroIndexes.append(i)
        i+=1
        n >>= 1
    return oneIndexes, zeroIndexes

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitCount = len(getBitIndexes(num2)[0])
        num1Indexes, num1Zeros = getBitIndexes(num1)
        # We want to put a one where the num1Indexes are
        resultIndex = []
        for ni in reversed(num1Indexes):
            resultIndex.append(ni)
            bitCount -= 1
            if(bitCount == 0):
                break
        for ni in num1Zeros:
            if bitCount == 0:
                break
            resultIndex.append(ni)
            bitCount -= 1
        surplusBitIndex = num1Indexes[-1]+1
        while(bitCount):
            resultIndex.append(surplusBitIndex)
            bitCount -= 1
            surplusBitIndex += 1
        result = 0
        for f in resultIndex:
            result += (1 << f)
        return result
