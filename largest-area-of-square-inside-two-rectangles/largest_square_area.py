
def intersection(li, ri, lj, rj):
    li,ri = (min(li, ri), max(li, ri))
    lj,rj = (min(lj, rj), max(lj, rj))
    if (li > lj):
        li, ri, lj, rj = lj, rj, li, ri
    if ri <= lj:
        return 0
    return min(ri, rj) - lj 
        

class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        result = 0
        rectangles = [(b, l, t, r) for ((b, l), (t, r)) in zip(bottomLeft, topRight)]
        rectangles.sort(key= lambda r:0-abs((r[2]-r[0]) * (r[3]-r[1])))
        for i in range(len(bottomLeft)-1):
            ((bi, li), (ti, ri)) = (bottomLeft[i], topRight[i])
            for j in range(i+1, len(bottomLeft)):
                ((bj, lj), (tj, rj)) = (bottomLeft[j], topRight[j])
                vertical_intersection = intersection(bj, tj, bi, ti)
                if vertical_intersection == 0 or vertical_intersection < result:
                    continue
                result = max(
                    result,
                    min(
                        vertical_intersection,
                        intersection(lj, rj, li, ri)
                    )
                )
        return result * result
