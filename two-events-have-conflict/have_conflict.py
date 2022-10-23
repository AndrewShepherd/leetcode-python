def convert_to_minutes(s):
    return int(s[:2]) * 60 + int(s[3:])

def overlap(l1, r1, l2, r2):
    if r1 < l2:
        return False
    if r2 < l1:
        return False
    return True

class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        l1, r1 = [convert_to_minutes(s) for s in event1]
        l2, r2 = [convert_to_minutes(s) for s in event2]
        return overlap(l1, r1, l2, r2)
