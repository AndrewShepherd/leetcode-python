def getLine(p1, p2):
    g = (p2[1] - p1[1])/(p2[0] - p1[0])
    c = p1[1] - g * p1[0]
    return (g, c)

def getAdjacentPairs(l):
    for i in range(len(l)-1):
        yield l[i], l[i+1]

class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        stockPrices.sort()
        lines = [getLine(p1, p2) for p1,p2 in getAdjacentPairs(stockPrices)]
        if len(lines) == 0:
            return 0
        count = 1
        adjacentLines = list(getAdjacentPairs(lines))
        for i, p in enumerate(adjacentLines):
            if p[0] != p[1]:
                count += 1
            else:
                count += 0
        return count
