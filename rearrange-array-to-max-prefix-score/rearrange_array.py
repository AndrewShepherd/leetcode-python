class Solution:
    def maxScore(self, nums: list[int]) -> int:
        positive_count = 0
        positive_sum = 0
        zero_or_less = []
        
        for n in nums:
            if n > 0:
                positive_count += 1
                positive_sum += n
            else:
                zero_or_less.append(n)

        zero_or_less.sort(reverse=True)
        for n in zero_or_less:
            positive_sum += n
            if positive_sum > 0:
                positive_count += 1
            else:
                break
        return positive_count
