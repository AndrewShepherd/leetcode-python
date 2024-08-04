import math

def does_intersect(circle_one, circle_two):
    x1,y1,r1 = circle_one
    x2,y2,r2 = circle_two
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d <= (r1 + r2)

def contains_point(circle, x, y):
    x1,y1,r1 = circle
    d = math.sqrt((x1-x)**2 + (y1-y)**2)
    return d <= r1

class Solution:


    def canReachCorner(self, X: int, Y: int, circles: list[list[int]]) -> bool:
        intersecting_sets = []
        for c in circles:
            if contains_point(c, 0, 0):
                return False
            if contains_point(c, X, Y):
                return False
            intersecting_indexes = []
            for i,s in enumerate(intersecting_sets):
                for c2 in s:
                    if does_intersect(c, c2):
                        intersecting_indexes.append(i)
                        break
            if (len(intersecting_indexes)):
                while(len(intersecting_indexes) > 1):
                    i = intersecting_indexes.pop()
                    intersecting_sets[intersecting_indexes[0]].extend(intersecting_sets[i])
                    del intersecting_sets[i]
                intersecting_sets[intersecting_indexes[0]].append(c)
            else:
                intersecting_sets.append([c])
        for s in intersecting_sets:
            intersect_left = False
            intersect_right = False
            interset_bottom = False
            intersect_top = False
            for cX, cY, r in s:
                if r >= abs(cX):
                    intersect_left = True
                if r >= abs(X - cX):
                    intersect_right = True
                if r >= abs(cY):
                    interset_bottom = True
                if r >= abs(Y - cY):
                    intersect_top = True
            if intersect_left and intersect_right:
                return False
            if intersect_top and interset_bottom:
                return False
            if intersect_top and intersect_right:
                return False
            if intersect_left and interset_bottom:
                return False
        return True

        
