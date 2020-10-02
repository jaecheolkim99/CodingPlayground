"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/

[Problem]
Given a list of non negative integers, arrange them such that they form the largest number.

[Best]
class Solution(object):
    def largestNumber(self, nums):
        stringList=[]
        for num in nums:
            stringList.append(str(num))
        res=sorted(stringList, cmp=lambda a,b:cmp(b+a, a+b))
        if res[0] == '0':
            return '0'
        else:
            return "".join(res)
"""

class Solution(object):
    def largestNumber(self, nums):
        result = ""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
            result += str(nums[i])

        if (result[0] == '0'):
            return "0"
        else:
            return result

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10,2]))
