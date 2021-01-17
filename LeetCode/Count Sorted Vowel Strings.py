"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/

[BEST]
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        d = [[1] + [0] * 4 for _ in range(n)]
        for i in range(len(vowels)):
            d[0][i] = i+1
        
        for i in range(1, n):
            for j in range(1, len(vowels)):
                    d[i][j] += d[i][j-1] + d[i-1][j]
                    
        return d[-1][-1]
"""
class Solution(object):
    def countVowelStrings(self, n):
        result = {5:1}

        n = n - 1

        while n > 0:
            n_result = {}
            for k, v in result.items():
                for i in range(k):
                    if i+1 in n_result:
                        n_result[i+1] += v
                    else:
                        n_result[i+1] = v
            result = n_result
            n -= 1

        ret = 0
        for k, v in result.items():
            ret += (k * v)

if __name__ == '__main__':
    s = Solution()
    s.countVowelStrings(33)
