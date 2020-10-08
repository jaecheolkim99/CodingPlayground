"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3488/

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

[Best]
class Solution(object):
    # Binary Search
    # Time complexity: O(logN)
    # Space complexity: O(1)
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return -1
        left,right = 0, len(nums)-1
        while (left<=right):
            mid = left + (right - left)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        return -1