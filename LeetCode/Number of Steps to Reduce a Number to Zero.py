"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637/

[BEST]
class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            count += 1
        return count

"""
class Solution(object):
    def checkRecursive(self, num):
        if num == 0:
            return self.steps

        self.steps += 1

        if num % 2 == 0:
            self.checkRecursive(int(num/2))
        else:
            self.checkRecursive(int(num-1))
        return self.steps

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.steps = 0

        if num == 0:
            return 0

        return self.checkRecursive(num)