"""
https://leetcode.com/explore/featured/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

[BEST]
class Solution(object):
    def generateMatrix(self, n):
        current, max_val = 1, n**2
        i, j = 0, 0
        top, right, bottom, left = 0, n-1, n-1, 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        while current <= max_val:
            matrix[i][j] = current
            current += 1
            
            if i == top and j < right:
                j += 1
                if j == right: top += 1
                continue
            
            if j == right and i < bottom:
                i += 1
                if i == bottom: right -= 1
                continue
                
            if i == bottom and j > left:
                j -= 1
                if j == left: bottom -= 1
                continue
            
            if j == left and i > top:
                i -= 1
                if i == top: left += 1
            
        return matrix

"""
class Solution(object):
    def changeDirection(self, direction):
        direction = direction % 4

        if direction == 0:
            return 0, 1
        elif direction == 1:
            return 1, 0
        elif direction == 2:
            return 0, -1
        elif direction == 3:
            return -1, 0

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0]*n for _ in range(n)]

        x, y = 0, 0
        direction = 0
        max_num = n  * n + 1
        count = 1
        max_step = n + 1
        step = 1

        while count != max_num:
            matrix[x][y] = count
            count += 1
            step += 1
            inc_x, inc_y = self.changeDirection(direction)
            x += inc_x
            y += inc_y

            if step == max_step:
                if direction % 2 == 0:
                    max_step -= 1
                x -= inc_x
                y -= inc_y
                direction += 1
                inc_x, inc_y = self.changeDirection(direction)
                x += inc_x
                y += inc_y
                step = 1

        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))