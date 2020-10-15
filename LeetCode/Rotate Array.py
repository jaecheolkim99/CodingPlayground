"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


[Best Soluion]
class Solution(object):
    def rotate(self, nums, k):
      nums [:k] , nums[k:]=nums[len(nums) - k:],nums[:len(nums) - k]

"""
class Solution(object):
    def rotate(self, nums, k):
        for i in range(len(nums)-k, len(nums)):
            nums.insert(0, nums.pop(-1))
        
        return nums