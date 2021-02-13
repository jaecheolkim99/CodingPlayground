"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/

[BEST]
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Check if characters appear the same number of times in both strings
        if set(s)==set(t):
            for char in list(set(s)):
                if s.count(char)!=t.count(char):
                    return False
            return True
        
        return False

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict = {}
        
        for c in s:
            if c in sdict:
                sdict[c] += 1
            else:
                sdict[c] = 1
        
        for c in t:
            if c not in sdict:
                return False
            else:
                if sdict[c] == 0:
                    return False
                else:
                    sdict[c] -= 1
        
        for c in sdict:
            if sdict[c] != 0:
                return False
        
        return True