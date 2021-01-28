"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

[BEST]
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        heap=defaultdict(list)
        
        for i,row in enumerate(mat):
            for j,val in enumerate(row):
                heap[i-j].append(val)
        
        for key in heap:
            heap[key].sort(reverse=True)
            
        for i,row in enumerate(mat):
            for j,val in enumerate(row):
                mat[i][j]=heap[i-j].pop()
        
        return mat

"""
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        mrow = len(mat)
        mcol = len(mat[0])

        # check row first
        for row in range(mrow - 1):
            data = []
            c = 0
            r = row
            while r < mrow and c < mcol:
                data.append(mat[r][c])
                r += 1
                c += 1
            data.sort()

            c = 0
            r = row
            i = 0
            
            while r < mrow and c < mcol:
                mat[r][c] = data[i]
                r += 1
                c += 1
                i += 1

        # check column
        for col in range(1, mcol - 1):
            data = []
            c = col
            r = 0
            
            while r < mrow and c < mcol:
                data.append(mat[r][c])
                r += 1
                c += 1                
            data.sort()
            
            c = col
            r = 0
            i = 0
            
            while r < mrow and c < mcol:
                mat[r][c] = data[i]
                r += 1
                c += 1
                i += 1
        
        return mat