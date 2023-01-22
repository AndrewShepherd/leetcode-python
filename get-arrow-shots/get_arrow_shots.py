def get_overlap(p1, p2):
    s1,e1 = p1
    s2,e2 = p2
    r = (max(s1,s2), min(e1,e2))
    if r[0] > r[1]:
        return (-1, -1)
    return r
    

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count = 0
        range = (-1, -1)
        for p in points:
            range = get_overlap(range, p)
            if range == (-1, -1):
                range = p
                count += 1
        return count
        
