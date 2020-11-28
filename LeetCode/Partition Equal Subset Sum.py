"""
https://leetcode.com/submissions/detail/424883455/?from=/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3545/
https://leetcode.com/problems/partition-equal-subset-sum/solution/
[BEST]
class Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
        
        if total % 2 == 1:
            return False
        
        target = total // 2
        nums.sort()
        
        def dfs(nums, target):
            if target < 0:
                return False
            elif target == 0:
                return True
            
            m = {}
            n = len(nums)
            if n == 0:
                return False
            for i in range(n-1, -1, -1):
                if nums[i] in m:
                    continue
                if dfs(nums[:i], target-nums[i]):
                    return True
                m[nums[i]] = True
            return False
        return dfs(nums, target)


"""
class Solution(object):
    def canPartition(self, nums):
        if len(nums) < 2:
            return False

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        partition = [[True for i in range(len(nums) + 1)]
                     for j in range(total_sum // 2 + 1)]

        for i in range(len(nums) + 1):
            partition[0][i] = True

        for i in range(1, total_sum // 2 + 1):
            partition[i][0] = False

        for i in range(1, total_sum // 2 + 1):
            for j in range(1, len(nums) + 1):
                partition[i][j] = partition[i][j-1]

                if i >= nums[j -1]:
                    partition[i][j] = (partition[i][j] or partition[i - nums[j-1]][j-1])

        return partition[total_sum // 2][len(nums)]