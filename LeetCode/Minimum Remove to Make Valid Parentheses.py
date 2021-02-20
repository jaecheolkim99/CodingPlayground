"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/

[BEST]
    def minRemoveToMakeValid(self, s):
        c1 = 0
        c2 = 0
        for i in s:
            if i == '(':
                c1 += 1
            if i == ')':
                if c1 > 0:
                    c1 -= 1
                else:
                    c2 += 1
 
        if c1 > 0:
            s =  ''.join(s.rsplit('(', c1))
        if c2 > 0:
            s =  s.replace(')', '', c2)
        return s

"""
class Solution(object):
    def removeInvalidParentheses(self, s, opener, closer):
        new_s, cnt = "", 0
        for c in s:
            if c == opener:
                cnt += 1
            elif c == closer:
                if cnt < 1:
                    continue
                cnt -= 1
            new_s += c
        return new_s

    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = self.removeInvalidParentheses(s, '(', ')')
        result = self.removeInvalidParentheses(result[::-1], ')', '(')
        return result[::-1]