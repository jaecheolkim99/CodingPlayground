"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494/

[BEST]
class Solution(object):
    def rob(self, nums):        
        # def rob(arr):
        #     first, sec = 0, 0
        #     for i in range(len(arr)):
        #         first, sec = sec, max(first + nums[i], sec)
        #     return sec
        
        def rob(nums):
            sec = 0
            first = 0
            for current in nums:
                first, sec = sec, max(current + first, sec)
            return sec
        
        if not nums: return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob(nums[1:]), rob(nums[:-1])) 
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_dp(nums, 0, len(nums)-1), self.rob_dp(nums, 1, len(nums)))
        
    def rob_dp(self, nums, start, end):
        cur = 0
        last = 0
        
        for i in range(start, end):
            last, cur = cur, max(nums[i]+last, cur)
        return cur
