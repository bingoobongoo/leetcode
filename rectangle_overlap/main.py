class Rectangle:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def isIntersection(self, otherRectangle):
        upper_inter_y = min(self.y2, otherRectangle.y2)
        lower_inter_y = max(self.y1, otherRectangle.y1)
        if upper_inter_y - lower_inter_y <= 0:
            return False
        
        right_inter_x = min(self.x2, otherRectangle.x2)
        left_inter_x = max(self.x1, otherRectangle.x1)
        if right_inter_x - left_inter_x <= 0:
            return False

        return True
 

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        rect_1 = Rectangle(rec1[0], rec1[1], rec1[2], rec1[3])
        rect_2 = Rectangle(rec2[0], rec2[1], rec2[2], rec2[3])
        return rect_1.isIntersection(rect_2)

