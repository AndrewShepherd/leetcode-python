class Node:
    def __init__(self, value):
        self.value = value
        self.mustComeBefore = set()
        self.mustComeAfter = set()
        

def getOrder(k, conditions):
    conditionNodes = [Node(_+1) for _ in range(k)]
    for before, after in conditions:
        conditionNodes[before-1].mustComeBefore.add(after)
        conditionNodes[after-1].mustComeAfter.add(before)
    results = []
    availableNodes = [conditionNodes[i] for i in range(k) if not conditionNodes[i].mustComeAfter]
    while availableNodes:
        node = availableNodes.pop()
        results.append(node.value)
        for cnValue in node.mustComeBefore:
            otherNode = conditionNodes[cnValue-1]
            otherNode.mustComeAfter.remove(node.value)
            if not otherNode.mustComeAfter:
                availableNodes.append(otherNode)
    return results

class Solution:
    def buildMatrix(self, k: int, rowConditions, colConditions):
        rowOrders = getOrder(k, rowConditions)
        colOrders = getOrder(k, colConditions)

        if len(rowOrders) < k:
            return []

        if len(colOrders) < k:
            return []

        rowAndColumnIndexes = ([[0,0] for _ in range(k)])
        for i,v in enumerate(rowOrders):
            rowAndColumnIndexes[v-1][0] = i
        for i,v in enumerate(colOrders):
            rowAndColumnIndexes[v-1][1] = i

        result = [[0]*k for _ in range(k)]
        for i, (row, column) in enumerate(rowAndColumnIndexes):
            result[row][column] = i+1
        return result
        
