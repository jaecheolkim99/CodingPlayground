"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3572/

[BEST]
class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        for c in S:
            if c.isalpha():
                size += 1
            else:
                size *= int(c)
        
        for i in range(len(S)-1,-1,-1):
            K = K % size
            if K == 0 and S[i].isalpha():
                return S[i]
            
            if S[i].isalpha():
                size -= 1
            else:
                size /= int(S[i])

"""
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """        
        maxlen = len(S)
        
        size = 0
        
        for i in range(maxlen):
            if S[i].isdigit():
                size = size * int(S[i])
            else:
                size += 1
        
        for i in range(maxlen - 1, -1, -1):
            K = K % size
            
            if K == 0 and S[i].isalpha():
                return S[i]
            
            if S[i].isdigit():
                size = size // int (S[i])
            else:
                size -= 1