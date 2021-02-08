"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

[BEST]
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = S.find(C)
        ans = []

        for i in range(len(S)):
            if S[i] == C:
                index = i
            ans.append(abs(i - index))
        
        index = S.find(C, -1)
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                index = i
            
            ans[i] = min(ans[i], abs(i - index))
        return ans

"""
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """

        result = []
        c_idx = len(s) * (-1)

        for i in range(len(s)):
            if s[i] == c:
                c_idx = i
            result.append(i - c_idx)

        for i in reversed(range(len(s))):
            if s[i] == c:
                c_idx = i
            result[i] = min(result[i], abs(i-c_idx))
        return result

if __name__ == '__main__':
    s = Solution()
    s.shortestToChar("12345", '3')