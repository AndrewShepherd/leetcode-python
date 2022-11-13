class Node:
    def __init__(self, cost: int, factories: list[list[int]]):
        self.cost = cost
        self.factories = factories

def split(node: Node, robotLocation: int):
    leftFactoryIndex = None
    rightFactoryIndex = None
    for fIndex, (fLocation, fRemaining) in enumerate(node.factories):
        if fLocation > robotLocation:
            rightFactoryIndex = fIndex
            break
        else:
            leftFactoryIndex = fIndex
    if leftFactoryIndex != None:
        fLocation, fRemaining = node.factories[leftFactoryIndex]
        factoriesCopy = node.factories[:]
        if fRemaining == 1:
            del factoriesCopy[leftFactoryIndex]
        else:
            factoriesCopy[leftFactoryIndex] = (fLocation, fRemaining - 1)
        yield Node(node.cost + abs(robotLocation - fLocation), factoriesCopy)
    if rightFactoryIndex != None:
        fLocation, fRemaining = node.factories[rightFactoryIndex]
        factoriesCopy = node.factories[rightFactoryIndex:]
        if fRemaining == 1:
            del factoriesCopy[0]
        else:
            factoriesCopy[0] = (fLocation, fRemaining - 1)
        yield Node(node.cost + abs(robotLocation - fLocation), factoriesCopy)

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory = sorted(f for f in factory if f[1] > 0)

        initialNode = Node(cost = 0, factories = factory)
        nodes = [initialNode]
        while robot:
            r = robot.pop(0)
            nodes2 : list[Node] = []
            for n in nodes:
                splitResults = split(n, r)
                for n2 in splitResults:
                    matched = False
                    for i, n3 in enumerate(nodes2):
                        if n2.factories == n3.factories:
                            nodes2[i] = n2 if n2.cost < n3.cost else n3
                            matched = True
                            break
                    if not matched:
                        nodes2.append(n2)
                # TODO: Some kind of merge
            nodes = nodes2
        minNode = nodes[0]
        for n in nodes:
            if n.cost < minNode.cost:
                minNode = n
        return minNode.cost