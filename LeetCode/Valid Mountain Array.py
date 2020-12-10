"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

[BEST]
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        heig = max(A)
        peak = A.index(heig)
        if A.count(heig)>1:
            return False
        elif heig!=A[0] and heig!=A[-1]:
            incl = A[:peak]
            decl = A[peak:]
            if len(set(incl)) == len(incl) and len(set(decl)) == len(decl):
                if sorted(incl) == incl and sorted(decl,reverse=True) == decl:
                    return True
                else:
                    return False
            else:
                return False
"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """        
        if len(arr) < 3:
            return False
        
        i = 1
        
        while i<len(arr) and arr[i-1] < arr[i]:
            i += 1
        
        if i == 1 or i == len(arr):
            return False
        
        while i < len(arr) and arr[i-1] > arr[i]:
            i += 1
        
        return i == len(arr)

