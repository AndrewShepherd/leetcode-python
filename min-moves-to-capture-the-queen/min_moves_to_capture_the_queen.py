# Three scenarios

# Queen is directly in the path of the rook or the bishop, and they do not block one another (1 move)
# Queen is directly in the path of the rook or the bishop, but one blocks the other (2 moves)
# Queen is not directly in the path of either (2 moves)

class Solution:
    def minMovesToCaptureTheQueen(self, rr: int, rc: int, br: int, bc: int, qr: int, qc: int) -> int:        
        # Same horizontal line
        if rr == qr:
            if br == rr and min(rc, qc) < bc < max(rc, qc):
                return 2
            else:
                return 1
            
        # Same vertical line
        if rc == qc:
            if bc == rc and min(rr, qr) < br < max(rr, qr):
                return 2
            else:
                return 1
            
        # Bishop if on diagonal
        if (abs(br - qr) == (abs(bc - qc))):
            if (abs(rr - qr) == (abs(rc - qc))) and min(qr, br) < rr < max(qr, br) and min(qc, bc) < rc < max(qc, bc):
                return 2
            else:
                return 1
            
        return 2

