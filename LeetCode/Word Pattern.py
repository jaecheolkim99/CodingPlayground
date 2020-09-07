"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

[Best]
class Solution(object):
    def wordPattern(self, pattern, string):
        sentence = string.split(' ')
        print(sentence)
        if len(sentence) != len(pattern):
            return False
        dictionary = dict()
        for i in range(len(pattern)):
            if pattern[i] in dictionary.keys():
                if sentence[i] != dictionary[pattern[i]]:
                    return False
            else:
                if sentence[i] in dictionary.values():
                    return False
                dictionary[pattern[i]] = sentence[i]
        return True

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """        
        dict = {}        
        s_str = str.split()
        
        if len(pattern) != len(s_str):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dict.keys():
                if s_str[i] != dict[pattern[i]]:
                    return False
            else:
                if s_str[i] in dict.values():
                    return False
                dict[pattern[i]] = s_str[i]

        return True

if __name__ == '__main__':
    s = Solution()

    print(s.wordPattern("abba", "dog hello hello dog"))
    print(s.wordPattern("abba", "dog hello hello dsdg"))