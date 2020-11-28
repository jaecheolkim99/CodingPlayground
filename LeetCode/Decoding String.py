"""
https://leetcode.com/submissions/detail/422023867/?from=/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3536/

[BEST]
class Solution(object):
    def decodeString(self, s):
        stack = []; 
        curNum = 0; 
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        loopstack = []
        strstack = []
        result = ""        
        maxlen = len(s)
        i = 0
        
        while i < maxlen:
            num = 0
            
            if s[i] >= '0' and s[i] <= '9':
                while (s[i] >= '0' and s[i] <= '9'):
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                i -= 1
                loopstack.append(num)
            elif s[i] == '[':
                if s[i-1] < '0' or s[i-1] > '9':
                    loopstack.append(1)
                strstack.append(s[i])
            elif s[i] == ']':
                tmp = ""                
                loop = 0
                
                if (len(loopstack) != 0):
                    loop = loopstack.pop()
                
                while (len(strstack) != 0 and strstack[-1] != '['):
                    tmp = strstack.pop() + tmp
                
                if (len(strstack) != 0 and strstack[-1] == '['):
                    strstack.pop()
                
                for j in range(loop):
                    result = result + tmp
                
                for j in range(len(result)):
                    strstack.append(result[j])
                
                result = ""
            else:
                strstack.append(s[i])

            i += 1
        
        while len(strstack) != 0:
            result = strstack.pop() + result
        
        return result