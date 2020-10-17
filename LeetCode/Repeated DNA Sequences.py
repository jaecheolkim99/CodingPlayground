"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3498/

[BEST]
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        seen, output = set(), set()
        
        for start in range(n - L + 1):
            tmp = s[start: start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output

"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = {}
        real_result = []

        if len(s) < 10:
            return real_result

        for i in range(len(s) - 9):
            sub_s = s[i:i+10]
            if sub_s not in result:
                result[sub_s] = 1
            else:
                result[sub_s] += 1
            if result[sub_s] == 2:
                real_result.append(sub_s)

        return real_result