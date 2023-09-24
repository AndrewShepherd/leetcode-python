class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        # values_and_indexes = sorted([(n, i) for i,n in enumerate(maxHeights)], key=lambda t:0-t[0])
        best_result = 0
        for index, value  in enumerate(maxHeights):
            this_result = value
            current = value
            for i in range(index-1, -1, -1):
                current = min(current, maxHeights[i])
                this_result += current
            current = value
            for i in range(index+1, len(maxHeights)):
                current = min(current, maxHeights[i])
                this_result += current
            best_result = max(this_result, best_result)
        return best_result
