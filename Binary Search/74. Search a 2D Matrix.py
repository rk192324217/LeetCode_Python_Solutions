class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if target in i:
                return True
            
        return False
                