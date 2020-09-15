"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5

[Best]
class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        if len(word) != 0:
            return(len(word[-1]))
        else:
            return 0
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()        
        if len(s) == 0:
            return 0        
        return len(s[-1])