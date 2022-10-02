from collections import defaultdict

class Solution:
    def equationsPossible(self, equations) -> bool:
        unequalRelationships = []
        d = defaultdict(set)
        for e in sorted(equations):
            l = e[0]
            r = e[-1]
            if(e[1] == '='):
                d[l].add(r)
                d[r].add(l)
            else:
                if (l==r): # contradiction
                    return False
                unequalRelationships.append((l, r))
        equalSets = []       
        while(d):
            toProcess = [list(d.keys())[0]]
            equalSet = set()
            while(toProcess):
                k = toProcess.pop()
                equalSet.add(k)
                if k in d:
                    others = d.pop(k)
                    for o in others:
                        if o not in equalSet:
                            equalSet.add(o)
                            toProcess.append(o)
            equalSets.append(equalSet)

        for l,r in unequalRelationships:
            matchingSet = None
            for s in equalSets:
                if l in s:
                    matchingSet = s
                    break
            if matchingSet != None and r in matchingSet:
                return False
        return True
            
