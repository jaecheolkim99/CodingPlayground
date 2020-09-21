"""
  Unique Paths III : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3466/

Solution
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.




[Best Solution]
class Solution(object):
    
    def uniquePathsIII(self, grid):
        l0, l1 = len(grid), len(grid[0])
        s = sum(sum(l) for l in grid)
        V = l0*l1 + s - 3 - 2
        
        for i, l in enumerate(grid):
            if 1 in l:                s0, s1 = i, l.index(1)
            if 2 in l:                e0, e1 = i, l.index(2)
        
        def sub(x, y, g, v):
#            print v, g
            retC = 0
            if v==V and abs(x-e0)+abs(y-e1)==1:
                return 1
            if x+1<l0 and g[x+1][y]==0:
#                gridN = copy.deepcopy(g)
#                gridN[x+1][y] = -1
#                retC += sub(x+1, y, g, v+1)
                g[x+1][y] = -1
                retC += sub(x+1, y, g, v+1)
                g[x+1][y] = 0
            if x>0 and g[x-1][y]==0:
#                gridN = copy.deepcopy(g)
#                gridN[x-1][y] = -1
#                retC += sub(x-1, y, gridN, v+1)
                g[x-1][y] = -1
                retC += sub(x-1, y, g, v+1)
                g[x-1][y] = 0
            if y+1<l1 and g[x][y+1]==0:
#                gridN = copy.deepcopy(g)
#                gridN[x][y+1] = -1
#                retC += sub(x, y+1, gridN, v+1)
                g[x][y+1] = -1
                retC += sub(x, y+1, g, v+1)
                g[x][y+1] = 0
            if y>0 and g[x][y-1]==0:
#                gridN = copy.deepcopy(g)
#                gridN[x][y-1] = -1
#                retC += sub(x, y-1, gridN, v+1)
                g[x][y-1] = -1
                retC += sub(x, y-1, g, v+1)
                g[x][y-1] = 0
            return retC
            
        return sub(s0, s1, grid, 0)

"""

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        max_r = len(grid)        
        max_c = len(grid[0])        
        
        start = list()
        end = list()
        visited = set()
        empty = 0
        self.result = 0
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == 1:
                    start.append(r)
                    start.append(c)
                elif grid[r][c] == 2:                    
                    end.append(r)
                    end.append(c)
                elif grid[r][c] == 0:
                    empty += 1
        
        def dfs(pos_r, pos_c, visited, go):
            if pos_r == end[0] and pos_c == end[1]:
                if go == empty+1:
                    self.result += 1
                return
            
            if 0 <= pos_r < max_r and 0 <= pos_c < max_c and grid[pos_r][pos_c] != -1 and (pos_r, pos_c) not in visited:
                visited.add((pos_r, pos_c))
                for i, j in [(0,-1), (0,1), (1,0), (-1,0)]:
                    dfs(pos_r + i, pos_c + j, visited, go + 1)
                visited.remove((pos_r, pos_c))
        
        dfs(start[0], start[1], visited, 0)
        
        return self.result