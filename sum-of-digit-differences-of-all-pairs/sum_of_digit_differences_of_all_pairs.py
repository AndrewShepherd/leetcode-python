class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        counts = []
        for n in nums:
            count_index = 0
            while(n):
                if count_index == len(counts):
                    counts.append(dict())
                d = n % 10
                if d in counts[count_index]:
                    counts[count_index][d] += 1
                else:
                    counts[count_index][d] = 1
                n //= 10
                count_index += 1
        result = 0
        for d in counts:
            for n1 in range(0, 10):
                if n1 in d:
                    c1 = d[n1]
                    for n2 in range(n1+1, 10):
                        if n2 in d:
                            c2 = d[n2]
                            result += c1*c2 # * abs(n1-n2)
        return result
