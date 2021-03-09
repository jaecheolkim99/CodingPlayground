"""
https://leetcode.com/submissions/detail/465585092/?from=explore&item_id=3665

[BEST]
class Solution(object):
    def removePalindromeSub(self, s):
        l = len(s)
        if( l == 0 ):
            return 0
        if( s == s[::-1] ):
            return 1
        else:
            return 2

"""
class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        if self.isPalindrome(s):
            return 1
        return 2