from collections import defaultdict


####################################
# Thie function enumerates the nodes 
# making up the cycle including startNode
#
# Assumes that it is a cycle
# (Undefined behavior otherwise)
#
def nodesInCycle(edges, startNode):
    node = edges[startNode]
    included = {startNode, node}
    while node != startNode:
        next = edges[node]
        included.add(next)
        node = next
    return included


class Solution:
    def longestCycle(self, edges) -> int:

        # For each node, work out which 
        # other nodes are pointing to it
        pointingTo = defaultdict(set)
        for i,p in enumerate(edges):
            if p != -1:
                pointingTo[p].add(i)

        #######################################
        # Remove the nodes that are not
        # in a cycle
        danglingPointers = []
        for i in range(len(edges)):
            if i not in pointingTo:
                danglingPointers.append(i)
        while(danglingPointers):
            danglingPointer = danglingPointers.pop()
            itsPointingTo = edges[danglingPointer]
            if itsPointingTo == -1:
                continue
            s = pointingTo[itsPointingTo]
            if danglingPointer in s:
                s.remove(danglingPointer)
                if not s:
                    pointingTo.pop(itsPointingTo, None)
                    danglingPointers.append(itsPointingTo)
        
        if not pointingTo:
            return -1


        # Now find the longest cycle
        best = -1
        possible = set(pointingTo.keys())
        while(possible):
            c = nodesInCycle(edges, possible.pop())
            best = max(best, len(c))
            # Eliminate all of these nodes
            # so we don't calculate the same cycle
            possible = possible.difference(c)
        return best