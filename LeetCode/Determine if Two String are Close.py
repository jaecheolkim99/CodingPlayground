"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/

[BEST]
import collections
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        w1_set, w2_set = set(word1), set(word2)
        if w1_set != w2_set:
            return False
        w1_c = []
        w2_c = []
        
        for w in w1_set:
            w1_c.append(word1.count(w))
        for w in set(w2_set):
            w2_c.append(word2.count(w))
            
        return sorted(w1_c) == sorted(w2_c)
"""
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        set1 = set()
        set2 = set()

        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        a = ord('a')

        for i in range(len(word1)):
            set1.add(word1[i])
            cnt1[ord(word1[i]) - a] += 1

        for i in range(len(word2)):
            set2.add(word2[i])
            cnt2[ord(word2[i]) - a] += 1

        cnt1.sort()
        cnt2.sort()

        return set1 == set2 and cnt1 == cnt2