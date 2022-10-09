class Solution:
    def findArray(self, pref):
        result = pref[:]
        s = pref[0]
        for i in range(1, len(pref)):
            thisValue = s ^ pref[i]
            result[i] = thisValue
            s = s ^ thisValue
        return result