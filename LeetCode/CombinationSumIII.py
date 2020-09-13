"""
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

example1
Input: k = 3, n = 7
Output: [[1,2,4]]

example2
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

[BEST]
class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dfs(candidates, 0, res, [], k, n)
        return res
    def dfs(self, nums, index, res, path, k, n):
        if k == 0 and n == 0:
            res.append(path)
            return
        if k < 0 or n < 0:
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, res, path + [nums[i]], k-1, n-nums[i])

"""

class Solution(object):
    def combinationSum3BackTrack(self, k, n, start, sum, result, temp):
        if k < 0:
            return
        if k == 0 and sum == n:
            result.append(list(temp))
            return
        while start < 10 and n >= sum+start:
            temp.append(start)
            self.combinationSum3BackTrack(k-1, n, start+1, sum+start, result, temp)
            temp.pop()
            start += 1
    def combinationSum3(self, k, n):
        result = []
        self.combinationSum3BackTrack(k, n, 1, 0, result, [])
        return result

if __name__ == '__main__':
    s = Solution()

    print(s.combinationSum3(3, 9))