class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        f_rx = ax2 - ax1
        f_ry = ay2 - ay1
        
        s_rx = bx2 - bx1
        s_ry = by2 - by1
        
        f_r, s_r = f_rx * f_ry, s_rx * s_ry
        res = f_r + s_r
        
        if bx1 > ax2 or by1 > ay2 or (bx1 < ax1 and bx2 < ax1) or (by1 < ay1 and by2 < ay1):
            return res
        
        cx1, cx2, cy1, cy2 = max(ax1, bx1),min(ax2, bx2),max(by1, ay1),min(ay2, by2)
        c_x = cx2-cx1
        c_y = cy2-cy1
        
        return res - c_x* c_y
        