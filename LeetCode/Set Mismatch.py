"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

[BEST]
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        set_sum = sum(set(nums))
        dup = sum(nums) - set_sum
        missing = (1+n)*n/2 - set_sum
        return [dup, missing]

"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeat = sum(nums) - sum(set(nums))
        loss = sum(range(1, len(nums)+1)) - sum(set(nums))
        return [repeat, loss]