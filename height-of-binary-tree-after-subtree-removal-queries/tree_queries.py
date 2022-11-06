# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class NodeData:

    def __init__(self, tree_node, distance_from_root, height_left, height_right):
        self.tree_node = tree_node
        self.height_left = height_left
        self.height_right = height_right
        self.parent_node = None
        self.height = max(height_left, height_right) + 1

def create_node_lookup(root):
    node_lookup = dict()

    def recursive_build(tn, distance_from_root = 0):
        if tn == None or tn.val == None:
            return None
        left_node = recursive_build(tn.left, distance_from_root+1)
        right_node = recursive_build(tn.right, distance_from_root+1)
        this_node = NodeData(
            tn,
            distance_from_root,
            left_node.height if left_node else -1,
            right_node.height if right_node else -1
        )
        if left_node:
            left_node.parent_node = this_node
        if right_node:
            right_node.parent_node = this_node
        node_lookup[tn.val] = this_node
        return this_node

    root_node = recursive_build(root)
    node_lookup[root.val] = root_node
    return node_lookup


class Solution:
    def treeQueries(self, root, queries: list[int]) -> list[int]:
        node_lookup = create_node_lookup(root)
        result = []
        for q in queries:
            removed_node = node_lookup[q]
            # Walk back up the tree to the top
            height = 0
            n = removed_node
            while(n):
                parent = n.parent_node
                if parent:
                    new_height = 0
                    

        return result