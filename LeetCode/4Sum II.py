"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/

[TEST]
import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count = 0
        sums = collections.defaultdict(int)
        for a in A:
            for b in B:
                sums[a + b] += 1
        for c in C:
            for d in D:
                if -d - c in sums:
                    count += sums[-d-c]
        return count
"""
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        maxloop = len(A)
        result = 0

        AB = {}
        for i in range(maxloop):
            for j in range(maxloop):
                sum = A[i] + B[j]
                if sum in AB:
                    AB[sum] += 1
                else:
                    AB[sum] = 1

        for i in range(maxloop):
            for j in range(maxloop):
                sum = (C[i] + D[j]) * -1
                if sum in AB:                    
                    result += AB[sum]
                    
        return result