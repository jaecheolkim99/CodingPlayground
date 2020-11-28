"""
https://leetcode.com/submissions/detail/423985921/?from=/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3543/

[BEST]
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        if K%2==0 or K%5==0: return -1

        v = 0
        for i in xrange(1,K+1):
            v = (v*10+1)%K
            if v == 0:return i
        
        return -1
"""
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        num = 0
        digit = 1
        
        for i in range(1, K+1):
            num = num * 10 + 1
            
            if num % K == 0:
                return digit
            digit += 1
        
        return -1