class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        s = 0
        onesToTake = min(numOnes, k)
        s += onesToTake
        k -= onesToTake
        for i in range(k):
            #if numOnes:
            #    numOnes -= 1
            #    s += 1
            if numZeros:
                numZeros -= 1
            elif numNegOnes:
                numNegOnes -= 1
                s -= 1
        return s