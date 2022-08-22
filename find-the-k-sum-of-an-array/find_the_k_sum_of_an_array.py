class Solution:
    def kSum(self, nums, k: int) -> int:
        sumPositives = sum(n for n in nums if n > 0)

        diffs = sorted([abs(n) for n in nums])

        subtractValues = [0]
        for n in diffs:
            newValues = []
            for p in subtractValues:
                newValue = p+n
                if len(subtractValues) == k and subtractValues[-1] < newValue:
                    break
                newValues.append(newValue)
            if not newValues:
                break
            subtractValues.extend(newValues)
            subtractValues.sort()
            del subtractValues[k:]
            
        return sumPositives - subtractValues[-1]
