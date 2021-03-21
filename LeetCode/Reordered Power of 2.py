"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/
"""
class Solution(object):
    def numToDict(self, N):
        result = {}
        cnt = 0
        for s in str(N):
            if s not in result:
                result[s] = 1
            else:
                result[s] += 1
            cnt += 1
        return result, cnt

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        num, cnt = self.numToDict(N)

        for i in range(30):
            poweroftwo, poweroftwocnt = self.numToDict(2 << i)

            if num == poweroftwo:
                return True
            if cnt < poweroftwocnt:
                return False
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(1521))