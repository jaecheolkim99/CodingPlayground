"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

[BEST]
class Solution(object):
    def distributeCandies(self, candyType):
        return min(len(candyType)//2, len(set(candyType)))
"""
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        candies = len(candyType)
        candies_set = set(candyType)
        if candies//2 < len(candies_set):
            return candies//2
        return len(candies_set)