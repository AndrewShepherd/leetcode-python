class Solution:
    def numberOfPairs(self, nums):
        pairs = 0
        left_over = 0
        last = None
        for n in sorted(nums):
            if last == None:
                last = n
            elif last == n:
                pairs += 1
                last = None
            else:
                left_over += 1
                last = n
        if last != None:
            left_over += 1
        return [pairs, left_over]