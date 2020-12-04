"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/

[BEST]
class Solution(object):
    def kthFactor(self, n, k):
        return solve(n, k)
    
from operator import mul

PS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def prime_factors(n):
    ret = []
    for p in PS:
        if n%p == 0:
            ret.append([p, 1])
            n /= p
            while n%p == 0:
                ret[-1][1] += 1
                n /= p
    if n != 1:
        ret.append([n, 1])
    return ret

def solve(n, k):
    if k == 1:
        return 1
    if k > n:
        return -1
    ps = prime_factors(n)
    cnts = [p[1]+1 for p in ps]
    maxk = reduce(mul, cnts)
    if k > maxk:
        return -1
    if k == maxk:
        return n
    ps = [p[0] for p in ps]
    factors = []
    for i in xrange(maxk):
        fac = 1
        for j, cnt in enumerate(cnts):
            i, rem = divmod(i, cnt)
            fac *= ps[j]**rem
        factors.append(fac)
    factors.sort()
    return factors[k-1]

[SECOND BEST]
class Solution(object):
    def kthFactor(self, n, k):
        i = 1
         
        lt = []
        ls = []
        
        while(i**2 < n):
            if n % i == 0:
                lt.append(i)
                ls.append(n//i)
            i += 1
            
        if i**2 == n:
            lst = lt + [i] + ls[::-1]
        else:
            lst = lt + ls[::-1]
            
        if k <= len(lst):
            return (lst)[k-1]
        
        return -1

"""
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i = 1
         
        lt = []
        ls = []
        
        while(i**2 < n):
            if n % i == 0:
                lt.append(i)
                ls.append(n//i)
            i += 1
            
        if i**2 == n:
            lst = lt + [i] + ls[::-1]
        else:
            lst = lt + ls[::-1]
            
        if k <= len(lst):
            return (lst)[k-1]
        
        return -1