"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3482/

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k

EXAMPLE
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

[BEST]
class Solution(object):
    def findPairs(self, nums, k):
        from collections import Counter
        numcnt = Counter(nums)
        
        res = 0
        for knum in numcnt:
            if k == 0:
                if numcnt[knum] > 1:
                    res += 1
            elif knum - k in numcnt:
                res += 1
        
        return res

"""
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = collections.Counter(nums)
        result = 0

        if k == 0:
            for key in c.keys():
                if c[key] > 1:
                    result += 1
        else:
            for key in c.keys():
                if key + k in c:
                    result += 1

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([1,2,1,2], 1))