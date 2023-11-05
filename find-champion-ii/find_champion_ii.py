class Solution:
    def findChampion(self, n: int, edges) -> int:
        hasParent = [False] * n
        for parent,child in edges:
            hasParent[child] = True
        result = None
        for i,v in enumerate(hasParent):
            if not v:
                if result != None:
                    return -1
                else:
                    result = i
        if result == None:
            return -1
        else:
            return result
    
