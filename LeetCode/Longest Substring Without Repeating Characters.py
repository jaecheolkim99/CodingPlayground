"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/

[BEST]
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0 
        maxlen = 0
        lookup = {}

        for index,c in enumerate(s):
            if c in lookup and start <= lookup[c]:
                start = lookup[c]+1
            else:
                maxlen = max(maxlen, index-start+1)
            lookup[c] = index

        return maxlen
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        last_loc_of_s = [-1]*256
        maxlength = 0

        for i in range(len(s)):
            left = max(left, last_loc_of_s[ord(s[i])] + 1)
            maxlength = max(maxlength, i - left + 1)
            last_loc_of_s[ord(s[i])] = i

        return maxlength

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))