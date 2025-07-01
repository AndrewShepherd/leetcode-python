class TreeNode:
    def __init__(self, value):
        self.children = []
        self.value = value

    def addChild(self, c):
        self.children.append(c)

    def evaluate(self) -> tuple[int, int]:
        if len(self.children) == 0:
            return (self.value, 0)
        
        max_child = 0
        total_leveling_cost = 0
        non_max_count = 0
        max_count = 0
        
        # Single pass: evaluate children and track max and counts
        for child in self.children:
            c, child_leveling_cost = child.evaluate()
            if c > max_child:
                # Previous max values become non-max
                non_max_count += max_count
                max_child = c
                max_count = 1
            elif c == max_child:
                max_count += 1
            else:  # c < max_child
                non_max_count += 1
            total_leveling_cost += child_leveling_cost
        
        return (max_child + self.value, total_leveling_cost + non_max_count)



class Solution:
    def minIncrease(self, n: int, edges: list[list[int]], cost: list[int]) -> int:
        treeNodes = [TreeNode(c) for c in cost]
        for p,c in edges:
            treeNodes[p].addChild(treeNodes[c])
        c,l = treeNodes[0].evaluate()
        return l
