"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3586/

[BEST]
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] % 2 == 0:
                    continue
                for di in [-1,0,+1]:
                    for dj in [-1,0,+1]:
                        if di == 0 and dj == 0: continue
                        if not 0 <= i+di < m or not 0 <= j+dj < n: continue
                        board[i+di][j+dj] += 2
        for i in range(m):
            for j in range(n):
                cnt = board[i][j] // 2
                if board[i][j] % 2:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                else:
                    if cnt == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        # Any live cell with fewer than two live neighbors dies as if caused by under-population.
         - underPopulation : fewer than two live neighbors
        # Any live cell with two or three live neighbors lives on to the next generation.
         - liveNext : two or three live neighbors
        # Any live cell with more than three live neighbors dies, as if by over-population.
         - overPopulation : more than three live neighbors
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
         - reproduct : with exactly three live neighbors        
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                countNeighborLive = sum((board[r][c] & 1) for r in range(row - 1, row + 2) for c in range(col - 1, col + 2)
                                        if (r, c) != (row, col) and 0 <= r < len(board) and 0 <= c < len(board[r]))
                if board[row][col] == 1:
                    if countNeighborLive < 2 or countNeighborLive > 3:
                        board[row][col] |= 2
                else:
                    if countNeighborLive == 3:
                        board[row][col] |= 2

        for row in range(len(board)):
            for col in range(len(board[row])):
                board[row][col] >>= 1

if __name__ == "__main__":
    s = Solution()
    s.gameOfLife([[0,0],[1,1]])