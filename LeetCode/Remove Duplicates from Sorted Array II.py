"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3562/

[BEST]
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=0
        while i+2<len(nums):
            if nums[i]==nums[i+2]:
                nums.pop(i+2)
            else:
                i=i+1
        return len(nums)
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = len(nums)
        duplicated = 2
        start = end = duplicated
        while end < maxlen:
            if nums[start - duplicated] != nums[end]:                
                nums[start] = nums[end]
                start += 1
            end += 1
        return start