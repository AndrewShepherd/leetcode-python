class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False

        pendingLs = 0
        pendingRs = 0
        for i in range(len(start)):
            s, t = start[i], target[i]
            if t == 'L':
                if pendingRs:
                    return False
                pendingLs += 1
            if s == 'L':
                if not pendingLs:
                    return False
                pendingLs -= 1
            if s == 'R':
                if pendingLs:
                    return False
                pendingRs += 1
            if t == 'R':
                if not pendingRs:
                    return False
                pendingRs -= 1
        return pendingLs == 0 and pendingRs == 0

