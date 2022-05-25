def getMaxLength(node):
    if node["maxLength"] != None:
        return node["maxLength"]
    maxLength = 1
    joining = node["joining"]
    if joining:
        maxLength += max([getMaxLength(n) for n in joining])
    node["maxLength"] = maxLength
    return maxLength

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nodes = [{ "joining": [], "maxLength": None} for e in envelopes]
        for i in range(len(envelopes) - 1):
            for j in range(i+1, len(envelopes)):
                iWidth, iHeight = envelopes[i]
                jWidth, jHeight = envelopes[j]
                if iWidth < jWidth:
                    if iHeight < jHeight:
                        nodes[i]["joining"].append(nodes[j])
                elif jWidth < iWidth:
                    if jHeight < iHeight:
                        nodes[j]["joining"].append(nodes[i])
        return max([getMaxLength(n) for n in nodes])
        