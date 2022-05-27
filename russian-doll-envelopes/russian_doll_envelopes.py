

def lis(values):
    # Start point, length
    if len(values) == 1:
        return 1
    entries = [values.pop(0)]
    
    for v in values:
        if v <= entries[0]:
            entries[0] = v
        elif v > entries[-1]:
            entries.append(v)
        else:
            for i in range(1, len(entries)):
                if v > entries[i-1] and v <= entries[i]:
                    entries[i] = v
                    break
    return len(entries) 

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if(len(envelopes) == 0):
            return 0
        envelopes = sorted(envelopes, key=lambda e:[e[0], e[1]*-1])
        i = 1
        while i < len(envelopes):
            if envelopes[i] == envelopes[i-1]:
                envelopes.pop(i)
            else:
                i += 1
        
        if(len(envelopes) == 1):
            return 1

        return lis([e[1] for e in envelopes])