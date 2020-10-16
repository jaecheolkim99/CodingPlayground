"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/

[BEST]
class Solution(object):
    def searchMatrix(self, matrix, target):        
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        lo, hi = 0, m*n-1
        
        if hi == 0:
            return matrix[0][0] == target
        
        while lo <= hi:
            mid = lo + (hi-lo)//2
            mid_i, mid_j = divmod(mid,n)
            if target == matrix[mid_i][mid_j] :
                return True
            elif target > matrix[mid_i][mid_j]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False
"""
class Solution(object):
    def searchMatrix(self, matrix, target):        
        if not matrix or len(matrix[0]) == 0:
            return False
        
        y = len(matrix[0]) - 1

        def binSearch(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high

        for x in range(len(matrix)):
            y = binSearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False
