class Solution:
    def minimumOperations(self, nums: list[int], target: list[int]) -> int:
        score = 0
        diffs = [t-n for t,n in zip(nums, target)]
        s = [0]

        def make_level():
            t = abs(s[-1])
            del s[1:]
            return t

        for d in diffs:
            if d == s[-1]:
                continue
            elif s[-1] == 0:
                s.append(d)
            elif d == 0:
                score += make_level()
            elif (s[-1] < 0) != (d < 0):
                score += make_level()
                s.append(d)
            elif d > 0 and d > s[-1]:
                s.append(d)
            elif d < 0 and d < s[-1]:
                s.append(d)
            elif d < 0 and d > s[-1]:
                score += abs(d-s[-1])
                while s[-1] <= d:
                    s.pop()
                s.append(d)
            elif d > 0 and d < s[-1]:
                score += abs(d-s[-1])
                while s[-1] >= d:
                    s.pop()
                s.append(d)
            else:
                raise(Exception("Unexpected case"))
        score += make_level()
        return score