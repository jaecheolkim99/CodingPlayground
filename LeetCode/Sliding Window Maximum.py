"""
https://leetcode.com/submissions/detail/424921266/?from=/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3546/

[BEST]
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        for i in range(len(nums)-k+1):
            if i == 0:
                m = max(nums[i:k+i])
            else:
                if nums[i-1] == m:
                    if m-1 != nums[i]:
                        m = max(nums[i:k+i])
                    else:
                        m = max(m-1,nums[k+i-1])
                else:
                    m = max(m,nums[k+i-1])
                        
            ans.append(m)
            
        return ans
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        maxval = max(nums[0:k])
        result.append(maxval)

        for i in range(1, len(nums) - k + 1):
            if nums[i-1] == maxval:
                maxval = max(nums[i:i+k])
            elif nums[i+k-1] > maxval:
                maxval = nums[i+k-1]
            result.append(maxval)

        return result