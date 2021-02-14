"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/

[BEST]
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if grid[0][0] or grid[m-1][n-1]: return -1
        
        ans = 0        
        q = [(0,0)]
        grid[0][0] = 1
        while q:
            ans += 1
            new_q = []
            for i,j in q:
                if i == m-1 and j == n - 1:
                    return ans
                if i > 0: 
                    if not grid[i-1][j]:
                        new_q.append((i-1,j))
                        grid[i-1][j] = 1
                    if j > 0 and not grid[i-1][j-1]:
                        new_q.append((i-1,j-1))
                        grid[i-1][j-1] = 1
                    if j < n - 1 and not grid[i-1][j+1]:
                        new_q.append((i-1, j + 1))
                        grid[i-1][j+1] = 1
                if i < m - 1:
                    if not grid[i+1][j]:
                        new_q.append((i+1,j))
                        grid[i+1][j] = 1
                    if j > 0 and not grid[i+1][j-1]: 
                        new_q.append((i+1,j-1))
                        grid[i+1][j-1] = 1
                    if j < n - 1 and not grid[i+1][j+1]: 
                        new_q.append((i+1, j+1))
                        grid[i+1][j+1] = 1
                if j > 0 and not grid[i][j-1]:
                    new_q.append((i, j - 1))
                    grid[i][j-1] =1 
                if j < n - 1 and not grid[i][j+1]:
                    new_q.append((i, j + 1))
                    grid[i][j+1] = 1
            q = new_q
        return -1

"""
from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)

        if grid[0][0] or grid[-1][-1] == 1:
            return -1

        queue = deque([[[0,0], 1]])
        visited = set((0,0))

        position = [[1,0],[1,1],[1,-1],[0,0],[0,1],[0,-1],[-1,0],[-1,1],[-1,-1]]
        cnt = 1

        while queue:
            pos, cnt = queue.popleft()
            if pos[0] == m - 1 and pos[1] == m - 1:
                return cnt
            for k in range(8):
                x = pos[0] + position[k][0]
                y = pos[1] + position[k][1]

                if 0 <= x < m  and 0 <= y < m and grid[x][y] == 0 and (x, y) not in visited:
                    visited.add((x,y))
                    queue.append([[x, y], cnt + 1])
        return -1