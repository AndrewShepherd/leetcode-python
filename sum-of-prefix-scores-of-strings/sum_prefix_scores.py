from collections import defaultdict



COUNT = 0

def makeTreeNode():
    return defaultdict(makeTreeNode)

class Solution:
    def sumPrefixScores(self, words):
        treeRoot = makeTreeNode()

        for w in words:
            currentNode = treeRoot
            for c in w:
                currentNode = currentNode[c]
                count = currentNode.get(COUNT, 0)
                currentNode[COUNT] = count + 1
        result = [0] * len(words)
        for i,w in enumerate(words):
            currentNode = treeRoot
            for c in w:
                currentNode = currentNode[c]
                result[i] += currentNode[COUNT]
        return result