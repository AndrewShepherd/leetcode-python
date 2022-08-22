import heapq
from collections import defaultdict

class JourneyDetails:
    def __init__(self, length: int, previous: str, index: int):
        self.length = length
        self.previous = previous
        self.index = index

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        visited = defaultdict(lambda: False)
        journeyDetails = dict()
        initial = "?" * len(target)
        journeyDetails[initial] = JourneyDetails(0, "", None)
        q = [(0, -1, initial)]
        while(q):
            l, _, s = heapq.heappop(q)
            if l > 10*len(target):
                return []
            if visited[s]:
                continue
            visited[s] = True
            for i in range(0, len(target)-len(stamp)+1):
                stampedString = s[0:i] + stamp + s[i+len(stamp):]
                if visited[stampedString]:
                    continue

                jd = JourneyDetails(l+1, s, i)
                if stampedString == target:
                    result = [jd.index]
                    while(jd.previous):
                        jd = journeyDetails[jd.previous]
                        if(jd.index == None):
                            return result
                        result = [jd.index] + result
                    return result
                if stampedString in journeyDetails:
                    existingDetails = journeyDetails[stampedString]
                    if existingDetails.length <= jd.length:
                        jd = existingDetails
                journeyDetails[stampedString] = jd
                heapq.heappush(q, (jd.length, jd.index, stampedString))
        return []

