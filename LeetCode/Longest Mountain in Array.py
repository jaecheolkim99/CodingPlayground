"""
https://leetcode.com/submissions/detail/420907922/?from=/explore/featured/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3533/

[BEST]
class Solution(object):
    def longestMountain(self, A):
        return solve(A)
    
def solve(a):
    n = len(a) - 1
    i = 1
    maxlen = l = 0
    while i < n:
        if a[i-1] >= a[i]:
            l = i
        elif a[i] > a[i+1]:
            for r in xrange(i+1, n):
                if a[r] <= a[r+1]:
                    if maxlen < r-l+1:
                        maxlen = r-l+1
                    i = l = r
                    break
            else:
                return max(maxlen, n-l+1)
        i += 1
    return maxlen

"""
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        increase = 0
        decrease = 0
        result = 0
        start = 0
        end = 0

        for i in range(1, len(A)):
            if (decrease > 0 and A[i] > A[i - 1]) or A[i] == A[i - 1]:
                decrease = increase = 0

            if A[i] > A[i - 1]:
                if increase != 1:
                    increase = 1
                    start = i - 1

            if A[i] < A[i - 1]:
                if decrease == 1:
                    end = i
                else:
                    decrease = 1
                    end = i

            if increase > 0 and decrease > 0:
                result = max(result, end  - start + 1)

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.longestMountain([2,1,4,7,3,2,5]))
    print(s.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))