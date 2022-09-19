# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        layer = [root]
        isEven = True
        while(layer):
            if not isEven:
                values = [node.val for node in layer]
                for n,v in zip(layer, reversed(values)):
                    n.val = v
            nextLayer = []
            for node in layer:
                if node.left:
                    nextLayer.extend([node.left, node.right])
            isEven = not isEven
            layer = nextLayer
        return root