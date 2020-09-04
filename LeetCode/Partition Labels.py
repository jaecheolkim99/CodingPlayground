"""
A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

"""
[BEST]
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i,c in enumerate(S)}
        anchor = j = 0
        ans = []
        for i,c in enumerate(S):
            j = max(j,last[c])
            #print("I",i,"C",c,"J",j)
            if i==j:
                #print("i-anchor + 1",i-anchor + 1)
                ans.append(i-anchor + 1)
                anchor = i+1
        return ans
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return 0

        ret = []
        start, end = 0, 0

        for i in range(len(S)):
            end = max(end, S.rfind(S[i]))
            if i == end:
                ret.append(end - start + 1)
                start = end + 1

        return ret
