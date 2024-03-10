class TreeNode:

    def __init__(self, min_value, max_value_exclusive):
        self.min_value = min_value
        self.max_value_exclusive = max_value_exclusive
        self.count = 0
        self.left = None
        self.right = None
        self.exact_match_count = 0

    def add(self, value):
        my_value = (self.max_value_exclusive + self.min_value)//2
        if value == my_value:
            self.exact_match_count += 1
        elif value < my_value:
            if self.left == None:
                self.left = TreeNode(self.min_value, my_value)
            self.left.add(value)
        else:
            if self.right == None:
                self.right = TreeNode(my_value + 1, self.max_value_exclusive)
            self.right.add(value)
        self.count += 1

    def count_of_values_greater_than(self, n):
        if self.min_value > n:
            return self.count
        if self.max_value_exclusive <= n:
            return 0
        my_value = (self.max_value_exclusive + self.min_value)//2
        result = 0
        if my_value > n:
            result += self.exact_match_count
        if self.left:
            result += self.left.count_of_values_greater_than(n)
        if self.right:
            result += self.right.count_of_values_greater_than(n)
        return result   


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        min_value = min(nums)
        max_value = max(nums)

        lNode = TreeNode(min_value, max_value + 1)
        rNode = TreeNode(min_value, max_value + 1)

        l,r = nums[:1], nums[1:2]
        lNode.add(nums[0])
        rNode.add(nums[1])

        for index in range(2, len(nums)):
            n = nums[index]
            gL = lNode.count_of_values_greater_than(n)
            gR = rNode.count_of_values_greater_than(n)
            if gL > gR:
                l.append(n)
                lNode.add(n)
            elif gR > gL:
                r.append(n)
                rNode.add(n)
            elif len(l) <= len(r):
                l.append(n)
                lNode.add(n)
            else:
                r.append(n)
                rNode.add(n)
        return l + r
