from collections import Counter

def ip(items, totalPlaces):
    if items == 0:
        yield []
    else:
        for place in range(totalPlaces - items + 1):
            for subPlaces in ip(items-1, totalPlaces - place - 1):
                yield [place] + [p+place+1 for p in subPlaces]
            
def place(startList, n, nIndexes):
    newList = [None] * (len(startList) + len(nIndexes))
    si = 0 
    ni = 0
    for nLi in range(len(newList)):
        if ni < len(nIndexes) and nIndexes[ni] == nLi:
            newList[nLi] = n
            ni += 1
        else:
            newList[nLi] = startList[si]
            si += 1
    return newList

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        c = Counter(nums)
        distinctNums = list(c.keys())
        
        def p(index):
            if index == len(distinctNums):
                yield []
            else:
                n = distinctNums[index]
                nCount = c[n]
                
                for combo in p(index+1):
                    for indexPermutation in ip(nCount, nCount + len(combo)):
                        yield place(combo, n, indexPermutation)
        return list(p(0))