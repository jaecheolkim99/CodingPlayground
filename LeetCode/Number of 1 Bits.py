"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

[BEST]
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ret = 0
        # while n:
        #     n &= n-1
        #     ret += 1
        # return ret
        return bin(n).count('1')

"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        strn = str(bin(n))
        cnt = Counter(strn)
        
        if '1' in cnt:
            return cnt['1']
        return 0
        