"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/

"""
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 = str2 = ""

        for c in word1:
            str1 += c
        for c in word2:
            str2 += c

        if str1 == str2:
            return True
        return False
if __name__ == '__main__':
    s = Solution()
    s.arrayStringsAreEqual(["a","b","cd"], ["ab","cd"])