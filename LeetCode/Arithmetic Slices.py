"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/

[BEST]
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = [0]
        f = 1
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                res.append(res[-1]+f)
                f += 1
            else:
                f=1
        
        return res[-1]

"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        sum = 0

        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                count += 1
            else:
                sum = sum + ((count + 1) * count / 2)
                count = 0
        return sum + ((count + 1) * count / 2)