class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:

        if (sx == tx and sy == ty):
            return 0
        if (sx == 0) and (sy == 0):
            return -1



        if (sx > tx) or (sy > ty):
            return -1
        
        if (tx == ty):
            if sx > sy:
                sx,sy = sy,sx
            if sx == 0:
                if sy == ty:
                    return 1
                else:
                    sub_result = self.minMoves(sx, sy*2, tx, ty)
                    if (sub_result == -1):
                        return -1
                    else:
                        return sub_result + 1

        if tx > ty:
            sx, sy, tx, ty = sy, sx, ty, tx

        if ty > (tx<<1):
            if ty % 2 == 1:
                return -1
            sub_result = self.minMoves(sx, sy, tx, ty//2)
            if (sub_result == -1):
                return -1
            else:
                return 1 + sub_result
        
        sub_result = self.minMoves(sx, sy, tx, ty-tx)
        if (sub_result == -1):
            return -1
        else:
            return 1 + sub_result
    
