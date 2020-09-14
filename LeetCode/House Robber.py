"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

example
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

[BEST]
class Solution(object):
    def rob(self, nums):
        # base case
        if nums == []:
            return 0
        
        preMax, currMax = 0, 0
        for num in nums:
            tmp = currMax
            currMax = max(preMax+num, currMax)
            preMax = tmp
            
        return currMax
"""

class Solution(object):
    def rob(self, nums):
        now = 0
        last = 0
        for i in nums:
            last, now = now, max(i+last, now)
        return now