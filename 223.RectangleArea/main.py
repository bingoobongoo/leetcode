class Rectangle:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)
        self.area = abs(x1 - x2) * abs(y1 - y2)

    def intersectionArea(self, otherRectangle):
        upper_inter_y = min(self.y2, otherRectangle.y2)
        lower_inter_y = max(self.y1, otherRectangle.y1)
        right_inter_x = min(self.x2, otherRectangle.x2)
        left_inter_x = max(self.x1, otherRectangle.x1)
        
        y_diff = upper_inter_y - lower_inter_y
        x_diff = right_inter_x - left_inter_x

        if y_diff <= 0 or x_diff <= 0:
            return 0

        return y_diff * x_diff

class Solution:
    def computeArea(self, ax1 , ay1 , ax2 , ay2 , bx1 , by1 , bx2 , by2 ):
        rect_1 = Rectangle(ax1, ay1, ax2, ay2)
        rect_2 = Rectangle(bx1, by1, bx2, by2)

        totalArea = rect_1.area + rect_2.area - rect_1.intersectionArea(rect_2)
        return totalArea
        