"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

[Best]
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = 0
        for i in dic:
            if i + 1 in dic:
                result = max(result, dic[i] + dic[i + 1])
        return result

"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                dict[num].append(i)
            else:
                dict[num] = [i]

        dict = sorted(dict.items())

        result = 0
        prevkey = None
        prevlen = 0
        for key, val in dict:
            if prevkey == None:
                prevkey = key
                prevlen = len(val)
                continue
            if key - prevkey == 1:
                result = max(result, len(val) + prevlen)
            prevlen = len(val)
            prevkey = key

        return result