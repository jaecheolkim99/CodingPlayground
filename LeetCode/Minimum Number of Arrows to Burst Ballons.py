"""
[Problem]
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3490/

[Best]
class Solution(object):
    def findMinArrowShots(self, points):
        sorted_p = sorted(points, key=lambda x: x[1])
        shots = []

        for p in sorted_p:
            if len(shots)==0:
                shots.append(p[1])
            elif shots[-1]<p[0]:
                shots.append(p[1])
        return len(shots)
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0:
            return 0

        points = sorted(points, key=lambda x:x[1])

        start = points[0]
        result = 1

        for p in points:
            #print(p)
            if p[0] > start[1]:
                start = p
                result += 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

