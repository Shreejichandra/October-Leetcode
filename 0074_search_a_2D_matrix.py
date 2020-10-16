'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 '''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return False
        
        for i in range(len(matrix)):
            row_length = len(matrix[i])
            if matrix[i][0] <= target <= matrix[i][-1]:
                for j in range(row_length):
                    if matrix[i][j] == target:
                        return True
                    if matrix[i][j] > target:
                        return False
                    
            else:
                i += 1 
        
