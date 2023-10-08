class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        tasks.sort(key=lambda n:0-n)
        processorTime.sort()
        result = 0
        for ip, tp in enumerate(processorTime):
            for j in range(ip*4, (ip+1)*4):
                result = max(result, tp + tasks[j])
        return result
