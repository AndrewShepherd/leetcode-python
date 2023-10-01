

class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        downward_results = [0] * len(maxHeights)
        
        s = []
        running_total = 0
        for i, n in enumerate(maxHeights):
            nCount = 1
            while(s and s[-1][0] >= n):
                sValue, sCount = s.pop()
                running_total -= (sValue * sCount)
                nCount += sCount
            running_total += (nCount * n)
            s.append((n, nCount))
            downward_results[i] = running_total

        upward_results = [0] * len(maxHeights)
        s = []
        running_total = 0
        for i in range(len(maxHeights) - 1, -1, -1):
            n = maxHeights[i]
            nCount = 1
            while(s and s[-1][0] >= n):
                sValue, sCount = s.pop()
                running_total -= (sValue * sCount)
                nCount += sCount
            running_total += (nCount * n)
            s.append((n, nCount))
            upward_results[i] = running_total

        best_result = 0
        for i,n in enumerate(maxHeights):
            best_result = max(best_result, downward_results[i] + upward_results[i] - n)
        return best_result
