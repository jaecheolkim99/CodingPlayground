"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2
Input: "aba"
Output: False

Example 3
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


"""
[BEST]
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1:-1]
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_len = len(s)

        for n in range((int)(m_len / 2)):
            j = n + 1
            if (m_len % j == 0):
                for k in range(j, m_len, j):
                    if (s[0:j] != s[k:k + j]):
                        break
                    if (j == m_len - k):
                        return "true"
        return "false"

if __name__ == '__main__':
    s = Solution()

    print(s.repeatedSubstringPattern("ababab"))
