from collections import defaultdict

class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:

        dices = [
            range(1, 7),
            range(1, 7),
            range(1, 7),
            range(1, 5)
        ]
        d = defaultdict(int)
        d[0] = 1
        for r in dices:
            d2 = defaultdict(int)
            for roll in r:
                for k,v in d.items():
                    d2[k+roll] += v
            d = d2
            sum_values = sum(d.values())
        
        totalRolls = sum(d.values())
        total15orless = sum(v for k,v in d.items() if k <= 15)
        total16orMore = sum(v for k,v in d.items() if k >= 16)
        total17orless = sum(v for k,v in d.items() if k <= 17)
        prob1 = total16orMore/totalRolls
        prob2 = total17orless/totalRolls
        


        transforms = [0] * (len(nums) + 1)
        queries_index = 0
        t = 0
        for i,n in enumerate(nums):
            t += transforms[i]
            while n > t:
                if queries_index == len(queries):
                    return -1
                range_start, range_end, value = queries[queries_index]
                queries_index += 1
                if range_end < i:
                    continue
                if range_start <= i:
                    t += value
                else:
                    transforms[range_start] += value
                transforms[range_end + 1] -= value
        return queries_index

