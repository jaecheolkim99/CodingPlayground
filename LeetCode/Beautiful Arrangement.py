"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/

[BEST]
cache = {}
class Solution(object):
    def countArrangement(self, N):
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in xrange(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))
"""
class Solution(object):
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def checkArrangement(self, nums, i):
        if i == len(nums):
            self.result += 1
            return

        for j in range(i, len(nums)):
            if nums[j] % (i+1) == 0 or (i+1) % nums[i] == 0:
                self.swap(nums, i, j)
                self.checkArrangement(nums, i+1)
                self.swap(nums, i, j)

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0

        nums = [ i + 1 for i in range(n) ]
        self.checkArrangement(nums, 0)
        return self.result

if __name__ == '__main__':
    s = Solution()
    s.countArrangement(3)