class Solution:
    def hardestWorker(self, n: int, logs) -> int:
        startTime = 0
        maxDuration = -1
        bestEmployee = n+1
        for employeeId, taskEnd in logs:
            taskDuration = taskEnd - startTime
            if taskDuration > maxDuration:
                bestEmployee = employeeId
                maxDuration = taskDuration
            elif taskDuration == maxDuration:
                bestEmployee = min(employeeId, bestEmployee)
            startTime = taskEnd
        return bestEmployee