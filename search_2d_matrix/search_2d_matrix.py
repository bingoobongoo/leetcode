class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_low = 0
        row_high = len(matrix) - 1
        target_row = None
        while row_low <= row_high:
            row_middle = row_low + (row_high - row_low) // 2
            if target >= matrix[row_middle][0] and target <= matrix[row_middle][-1]:
                target_row = row_middle
                break
            if target > matrix[row_middle][0]:
                row_low = row_middle + 1
            else:
                row_high = row_middle - 1
                
        if target_row == None:
            return False
        
        col_low = 0
        col_high = len(matrix[target_row]) - 1
        while col_low <= col_high:
            col_middle = col_low + (col_high - col_low) // 2
            if target == matrix[target_row][col_middle]:
                return True
            if target > matrix[target_row][col_middle]:
                col_low = col_middle + 1
            else:
                col_high = col_middle - 1
        
        return False
                
obj = Solution()
ans = obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
print(ans)
        