def findClosetUnvisited(allTimes, visited):
    closestUnvisitedIndex = None
    hasNone = False
    for i, e in enumerate(allTimes):
        if visited[i]:
            continue
        if e == None:
            hasNone = True
            continue
        if closestUnvisitedIndex == None:
            closestUnvisitedIndex = i
        else:
            if(e[0] < allTimes[closestUnvisitedIndex][0]):
                closestUnvisitedIndex = i
    return closestUnvisitedIndex, hasNone

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        allTimes = [None]*n
        visited = [False]*n
        stack = [k]
        allTimes[k-1] = (0, k) # Distance, via

        while True:
            # Find the closest unvisited
            closestUnvisitedIndex, hasNone = findClosetUnvisited(allTimes, visited)
            if closestUnvisitedIndex == None:
                if hasNone:
                    return -1
                else:
                    return max([t[0] for t in allTimes])
            visited[closestUnvisitedIndex] = True
            for e in times:
                nodeFrom = e[0]
                if nodeFrom == closestUnvisitedIndex + 1:
                    nodeTo = e[1]
                    distance = e[2]
                    index = nodeTo-1
                    if visited[index]:
                        continue
                    distanceViaThisNode = allTimes[nodeFrom-1][0] + distance
                    if (allTimes[index] == None) or allTimes[index][0]>distanceViaThisNode:
                        allTimes[index] = distanceViaThisNode, nodeFrom
        