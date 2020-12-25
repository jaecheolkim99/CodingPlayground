"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3580/

"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M = len(matrix)
        N = len(matrix[0])

        self.direction = 0
        result = []

        i = j = 0

        while True:
            result.append(matrix[i][j])

            if i == M - 1 and j == N - 1:
                break

            if self.direction == 0:
                if j == N - 1:
                    i += 1
                    self.direction = 1
                else:
                    i -= 1
                    j += 1
                    if i < 0:
                        i = 0
                        self.direction = 1
            else:
                if i == M - 1:
                    j += 1
                    self.direction = 0
                else:
                    i += 1
                    j -= 1
                    if j < 0:
                        j = 0
                        self.direction = 0
        return result