"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3500/

[BEST]
class Solution(object):
    def minDominoRotations(self, A, B):
        n = len(A)
        res = 0
        k = 0
        l = 1
        for i in range(n):
            if A[i]==B[i]:
                if A[i]!=res:
                    res=A[i]
                    k+=1
                else:
                    l+=1
            if k>1:
                return -1
        if res:
            if A.count(res)+B.count(res)==n+l:
                return n-max(A.count(res),B.count(res))
            return -1
            
        
        a = Counter(A)
        b = Counter(B)
        for i in range(1,7):
            if a[i]+b[i]>=len(A):
                return len(A)-max(a[i],b[i])
        return -1

"""
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        dominoCounter = collections.Counter(A) + collections.Counter(B)
        possible = []

        for item in dominoCounter:
            if dominoCounter[item] >= len(A):
                possible.append(item)

        if not possible:
            return -1

        result = len(A)

        def checkCount(A, B, count):
            low = 0
            high = 0
            for i in range(len(A)):
                if count == A[i] and count != B[i]:
                    high += 1
                elif count != A[i] and count == B[i]:
                    low += 1
                elif count != A[i] and count != B[i]:
                    return -1

            return min(low, high)

        for i in range(len(possible)):
            result = min(result, checkCount(A, B, possible[i]))

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
    #print(s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
