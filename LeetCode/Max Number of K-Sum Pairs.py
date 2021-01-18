"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/

[Best]
class Solution(object):
    def maxOperations(self, nums, k):
        numCount = defaultdict(int)
        for x in nums:
            numCount[x] += 1
        moves = 0
        for num, freq in numCount.iteritems():
            if k-num not in numCount:
                continue
            if k-num != num:
                moves += min(freq, numCount[k - num])
            else:
                moves += freq/2
            numCount[k-num] = 0
        
        return moves
"""
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_dic = {}
        operations = 0
        for n in nums:
            if n <= k:
                if k - n in nums_dic and nums_dic[k - n] > 0:
                    nums_dic[k-n] -= 1
                    operations += 1
                else:
                    if n in nums_dic:
                        nums_dic[n] += 1
                    else:
                        nums_dic[n] = 1
        return operations

if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([3,1,3,4,3], 6))
    print(s.maxOperations([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2))
    print(s.maxOperations([64,35,69,79,76,60,58,38,3,81,74,9,77,21,54,54,14,72], 47))