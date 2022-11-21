# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect


def closestNodesRecurisve(node, value) -> list[int]:
    if not node:
        return [-1, -1]
    if not node.val:
        return [-1, -1]
    if node.val == value:
        return [value, value]
    if value < node.val:
        minV, maxV = closestNodesRecurisve(node.left, value)
        return [minV, maxV if maxV != -1 else node.val]
    else:
        minV, maxV = closestNodesRecurisve(node.right, value)
        return [minV if minV != -1 else node.val, maxV]

class Solution:
    def closestNodes(self, root, queries: list[int]) -> list[list[int]]:

        queries_sorted = sorted([n, i] for i,n in enumerate(queries))
        sorted_values = [v for v,i in queries_sorted]
        sorted_indexes = [i for v,i in queries_sorted]
        result = [[-1, -1] for q in queries_sorted]

        def solve_recursive(node, l, rExclusive):
            if not node:
                return
            if not node.val:
                return
            if rExclusive <= l:
                return
            bl = bisect.bisect_left(sorted_values, node.val, l, rExclusive)
            br = bisect.bisect_right(sorted_values, node.val, bl, rExclusive)
            if 0 <= bl < len(sorted_values) and sorted_values[bl] == node.val:
                for i in range(bl, br):
                    result[i] = [node.val, node.val]
            solve_recursive(node.left, l, bl)
            for i in range(bl-1, l-1, -1):
                if result[i][1] != -1:
                    break
                result[i][1] = node.val
            solve_recursive(node.right, br, rExclusive)
            for i in range(br, rExclusive):
                if result[i][0] != -1:
                    break
                result[i][0] = node.val

        solve_recursive(root, 0, len(result))
        final_result = [None] * len(result)
        for target,v in zip(sorted_indexes, result):
            final_result[target] = v
        return final_result
