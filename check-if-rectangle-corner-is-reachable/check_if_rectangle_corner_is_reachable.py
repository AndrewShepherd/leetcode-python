import math


def point_falls_within_rectange(p, rect_width, rect_height):
    return 0 <= p[0] <= rect_width and 0 <= p[1] <= rect_height

def get_gradient_and_y_intercept(segment):
    ((x1, y1), (x2, y2)) = segment
    if (x2 == x1):
        return (math.inf, math.inf)
    g = (y2-y1)/(x2-x1)
    # y1 = g(x1) + c
    # c = y1 - g(x1)
    c = y1 - g * x1
    return (g, c)

def float_equal(f1, f2):
    return (abs(f1 - f2) < 0.00000001)

def point_falls_within_line_segment(p, segment):
    x,y = p
    (xStart, yStart), (xEnd, yEnd) = segment
    return min(xStart, xEnd) <= x <= max(xStart, xEnd) and min(yStart, yEnd) <= y <= max(yStart, yEnd)


def line_segments_overlap(segment1, segment2):
    g1, c1 = get_gradient_and_y_intercept(segment1)
    g2, c2 = get_gradient_and_y_intercept(segment2)
    if (float_equal(g1, g2)):
        # They are parallel
        if (float_equal(c1, c2)):
            # TODO: further check here
            return True
        else:
            return False
    x = (c2 - c1)/(g1 - g2)
    y = g1*x + c1
    return point_falls_within_line_segment((x,y), segment1) and point_falls_within_line_segment((x,y), segment2) 



def line_segment_overlaps_rectangle(segment, rect_width, rect_height):
    for p in segment:
        if point_falls_within_rectange(p, rect_width, rect_height):
            return True
    corners = [
        (0, 0),
        (rect_width, 0),
        (rect_width, rect_height),
        (0, rect_height)
    ]
    rect_lines = [(corners[i], corners[(i+1)%4]) for i in range(4)]
    for l in rect_lines:
        if line_segments_overlap(segment, l):
            return True
    return False

def does_intersect(circle_one, circle_two, rect_width, rect_height):
    x1,y1,r1 = circle_one
    x2,y2,r2 = circle_two
    d_squared = ((x1-x2)**2 + (y1-y2)**2)
    if (d_squared > (r1 + r2)**2):
        return False
    return line_segment_overlaps_rectangle(((x1, y1), (x2, y2)), rect_width, rect_height)

def contains_point(circle, x, y):
    x1,y1,r1 = circle
    d_squared = (x1-x)**2 + (y1-y)**2
    return d_squared <= r1**2

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
                    if does_intersect(c, c2, X, Y):
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

        def does_cross_left(cX, cY, r):
            if 0 <= cY <= Y:
                return abs(cX) <= r
            elif cY < 0:
                return cY**2 + cX**2 <= r**2
            else:
                return (cY - Y)**2 + cX**2 <= r**2
            
        def does_cross_right(cX, cY, r):
            if 0 <= cY <= Y:
                return abs(cX - X) <= r
            elif cY < 0:
                return cY**2 + (cX-X)**2 <= r**2
            else:
                return (cY - Y)**2 + (cX-X)**2 <= r**2
            
        def does_cross_bottom(cX, cY, r):
            if 0 <= cX <= X:
                return abs(cY) <= r
            elif cX < 0:
                return cX**2 + (cY)**2 <= r**2
            else:
                return (cX - X)**2 + cY**2 <= r**2 
            
        def does_cross_top(cX, cY, r):
            if 0 <= cX <= X:
                if 0 <= cY <= Y:
                    return abs(cY - Y) <= r
                else:
                    return abs(cY - Y) < r
            elif cX < 0:
                return cX**2 + (cY-Y)**2 <= r**2
            else:
                return (cX - X)**2 + (cY-Y)**2 <= r**2 

        for s in intersecting_sets:
            intersect_left = False
            intersect_right = False
            intersect_bottom = False
            intersect_top = False
            for cX, cY, r in s:
                intersect_left |= does_cross_left(cX, cY, r)
                intersect_right |= does_cross_right(cX, cY, r)
                intersect_bottom |= does_cross_bottom(cX, cY, r)
                intersect_top |= does_cross_top(cX, cY, r)
            if intersect_left and intersect_right:
                return False
            if intersect_top and intersect_bottom:
                return False
            if intersect_top and intersect_right:
                return False
            if intersect_left and intersect_bottom:
                return False
        return True

        
