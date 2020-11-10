"""
https://leetcode.com/submissions/detail/418826218/?from=/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3526/

[BEST]
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flip_A = []

        for elem in range(len(A)):
            flip_A_lst = []
            A_lst = A[elem]
            for i in reversed(A[elem]):
                flip_A_lst.append(i ^ 1)
            flip_A.append(flip_A_lst)
        return flip_A

if __name__ == '__main__':
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
