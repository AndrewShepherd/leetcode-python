def getSubtractionIndex(stamp: str, source: str):
    findResult = source.find(stamp)
    if findResult != -1:
        return findResult
    for i in range(len(source)-len(stamp)+1):
        atLeastOneMatch = False
        for j,c in enumerate(stamp):
            sC = source[i+j]
            if sC == '?':
                continue
            elif sC == c:
                atLeastOneMatch = True
                continue
            else:
                atLeastOneMatch = False
                break
        if atLeastOneMatch:
            return i
    return -1

def dfs(stamp: str, current: str):
    if all(c == '?' for c in current):
        return []
    else:
        i = getSubtractionIndex(stamp, current)
        if i == -1:
            return None
        currentTransformed =  current[0:i] + "?"*len(stamp) + current[i+len(stamp):]
        result = dfs(stamp, currentTransformed)
        if result != None:
            return result + [i]
        else:
            return None
            

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        result = dfs(stamp, target)
        return [] if result == None else result
        

