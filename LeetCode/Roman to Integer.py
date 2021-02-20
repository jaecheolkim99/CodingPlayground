"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/

[BEST]
class Solution(object):
    def romanToInt(self, s):
        crt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 1: return crt[s]
        i  = 0
        rt = 0
        while True:
            x = crt[s[i]]
            if x < crt[s[i+1]]: rt -= x
            else: rt += x
            i += 1
            if i == len(s)-1:
                rt += crt[s[i]]
                break
        return rt
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        if len(s) == 1:
            return roman[s]

        for key in special:
            if key in s:
                number += special[key]
                s = s.replace(key, "")

        for i in range(len(s)):
            number += roman[s[i]]

        return number