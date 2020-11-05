"""
https://leetcode.com/submissions/detail/417070565/?from=/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3520/

[BEST]
- This is best solution

"""
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = 0
        even = 0
        for p in position:
            if p % 2 == 0: even+=1
            else: odd+=1
        return min(odd, even)
