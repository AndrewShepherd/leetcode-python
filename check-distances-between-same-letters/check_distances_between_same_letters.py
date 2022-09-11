class Solution:
    def checkDistances(self, s: str, distance) -> bool:
        s = [ord(c) - ord('a') for c in s]
        firstOccurences = [None] * 26
        for index,val in enumerate(s):
            if firstOccurences[val] == None:
                firstOccurences[val] = index
            else:
                lettersBetween = index-firstOccurences[val]-1
                if lettersBetween != distance[val]:
                    return False
        return True
