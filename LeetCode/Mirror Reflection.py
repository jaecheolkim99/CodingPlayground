"""
https://leetcode.com/submissions/detail/421282767/?from=/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3534/

[BEST]
class Solution(object):
    def mirrorReflection(self, p, q):
        # find the smallest n such that nq = kp 
        
        if q == 0:
            return 0 
        
        # LCD
        
        def gcd(a, b):
            if a > b:
                return gcd(a-b,b)
            elif a < b:
                return gcd(b-a,a)
            else:
                return a 
        
        lcm = (p*q)/gcd(p,q)
        
        n = lcm / q
        
        if n % 2 == 0:
            return 2 
        else:
            return (lcm/p) % 2

"""
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """        
        while p % 2 == 0 and q % 2 == 0:
            p/=2
            q/=2            
        
        if q%2==0 and p%2!=0:
            return 0
        if q%2==1 and p%2==0:
            return 2
        if q%2==1 and p%2!=0:
            return 1 