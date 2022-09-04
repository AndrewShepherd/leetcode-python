class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        travelM = 0
        travelP = 0
        travelG = 0
        collect = 0
        for i in range(len(garbage)-1, -1, -1):
            collect += len(garbage[i])
            for c in garbage[i]:
                if c == 'M' and not travelM:
                    travelM = sum(travel[j] for j in range(i))
                if c == 'P' and not travelP:
                    travelP = sum(travel[j] for j in range(i))
                if c == 'G' and not travelG:
                    travelG = sum(travel[j] for j in range(i))
        return collect + travelM + travelP + travelG
