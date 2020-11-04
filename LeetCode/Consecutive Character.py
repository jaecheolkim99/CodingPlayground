"""
https://leetcode.com/submissions/detail/416552335/?from=/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/

[BEST]
class Solution(object):
    def maxPower(self, s):
        currentLetter = s[0]
        
        counter = 0
        
        maxCounter = 0
        
        if len(s) == 1:
            return 1
        
        for i in s:
            if i == currentLetter:
                counter += 1
                if i == s[len(s)-1]:
                    print("yes")
                    if counter > maxCounter:
                        maxCounter = counter
                    
            else:
                currentLetter = i
                
                if counter > maxCounter:
                    maxCounter = counter
                    
                counter = 1
                   
        return maxCounter

"""
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """

        c = s[0]
        maxlen = 1
        curlen = 1

        for i in range(1, len(s)):
            if s[i] == c:
                curlen += 1
            else:
                curlen = 1
                c = s[i]

            if maxlen < curlen:
                maxlen = curlen

        return maxlen