"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3587/

[BEST]
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        end = len(heights)
        if end == 0:
            return 0
        maxarea = min(heights) * end
        stack = []
        i = 0

        while i < end:
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                lp = stack.pop()
                if len(stack) == 0:
                    rp = i
                else:
                    rp = i - stack[-1] - 1
                curarea = heights[lp] * rp
                maxarea = max(maxarea, curarea)

        while len(stack) > 0:
            lp = stack.pop()
            if len(stack) == 0:
                rp = i
            else:
                rp = i - stack[-1] - 1
            curarea = heights[lp] * rp
            maxarea = max(maxarea, curarea)

        return maxarea

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([5,4,1,2]))