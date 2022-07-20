def transform(nString, trim):
    return int(nString[0-trim:])



class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        answers = []
        for k, trim in queries:
            nums_trimmed = [transform(n, trim) for n in nums]
            sorted_list = sorted([e[::-1] for e in enumerate(nums_trimmed)])
            answers.append(sorted_list[k-1][1])
        return answers