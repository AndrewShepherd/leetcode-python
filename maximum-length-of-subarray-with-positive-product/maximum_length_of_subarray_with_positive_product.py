class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_positive = 0
        current_neg = 0
        current_pos = 0

        for n in nums:
            if n < 0:
                new_neg = current_pos + 1
                new_pos = current_neg + 1 if current_neg else 0
            elif n > 0:
                new_neg = current_neg + 1 if current_neg else 0
                new_pos = current_pos + 1
            else:
                new_neg, new_pos = 0, 0
            current_neg, current_pos = new_neg, new_pos
            max_positive = max(max_positive, current_pos)
        return max_positive