"""
LINK : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example#1
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.


[BEST]
class Solution(object):
    def isRobotBounded(self, instructions):
        # 0=N, 1=E, 2=S, 3=W
        direction = 0
        spot = [0,0]
        for i in instructions:
            # spots.add(spot)
            if i == 'L':
                direction = (direction-1) %4
            if i == 'R':
                direction = (direction+1) %4
            if i == 'G':
                if direction == 0:
                    spot = [spot[0], spot[1]+1]
                if direction == 1:
                    spot = [spot[0]+1, spot[1]]
                if direction == 2:
                    spot = [spot[0], spot[1]-1]
                if direction == 3:
                    spot = [spot[0]-1, spot[1]]    
        if spot == [0,0] or direction != 0:
            return True
        return False

"""

class Solution(object):
    class Point():
        x = 0
        y = 0

    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        move = [[0,1], [1,0], [0,-1], [-1,0]]   # N -> E -> S -> W
        direction = 0
        point = self.Point()

        for i in range(4):
            for j in range(len(instructions)):
                if instructions[j] == 'G':
                    point.x += move[direction][0]
                    point.y += move[direction][1]
                elif instructions[j] == 'L':
                    direction = (direction + 3) % 4
                elif instructions[j] == 'R':
                    direction = (direction + 1) % 4

            if point.x == 0 and point.y == 0:
                return True

        return False

if __name__ == '__main__':
    s = Solution();

    print(s.isRobotBounded("GL"))
    print(s.isRobotBounded("GGLLGG"))