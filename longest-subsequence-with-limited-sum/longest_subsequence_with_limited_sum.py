class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        results = [0]*len(queries)
        for n in nums:
            for i, q in enumerate(queries):
                if q >= n:
                    queries[i] -= n
                    results[i] += 1
        return results