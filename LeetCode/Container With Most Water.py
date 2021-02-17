"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/

[BEST]
class Solution(object):
    def maxArea(self, height):
        low=0
        high=len(height)-1
        m=0
        area=0
        while low<=high:
            if height[low]>height[high]:
                area=(high-low) * height[high]
                high-=1
            else:
                area=(high-low) * height[low]
                low+=1
            if m<area:
                m=area
        return m

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height) - 1
        maxarea = 0

        while start < end:
            if height[start] < height[end]:
                maxarea = max(maxarea, height[start]*(end-start))
                start += 1
            else:
                maxarea = max(maxarea, height[end]*(end-start))
                end -= 1
        return maxarea