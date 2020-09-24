"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3471/

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

[Best]
class Solution(object):
    def findTheDifference(self, s, t):
        for char in t:
            if char not in s or t.count(char) > s.count(char):
                return char

"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dic = {}
        t_dic = {}

        for i in range(len(s)):
            if s[i] not in s_dic:
                s_dic[s[i]] = 1
            else:
                s_dic[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in t_dic:
                t_dic[t[i]] = 1
            else:
                t_dic[t[i]] += 1


        for key in t_dic:
            if key not in s_dic:
                return key
            elif t_dic[key] != s_dic[key]:
                return key

if __name__ == '__main__':
    s = Solution()

    print(s.findTheDifference('a','ab'))
