"""
https://leetcode.com/submissions/detail/423667673/?from=/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3542/

[BEST #1]
class Solution(object):
    def calculate(self, s):
        return eval(s)

[BEST #2]
class Solution(object):
    def calculate(self, s):
        if not s:
            return
        num = last_num = res = 0
        pre_op = '+'
        for i, cur in enumerate(s):
            if cur.isdigit():
                num = 10 * num + ord(cur) - ord('0')
            if i == len(s) - 1 or cur in '+-*/':
                if pre_op == '+' or pre_op == '-':
                    res += last_num
                    last_num = num if pre_op == '+' else -num
                elif pre_op == '*':
                    last_num *= num
                elif pre_op == '/':
                    if last_num < 0:
                        last_num = -(-last_num/num)
                    else:
                        last_num /= num
                pre_op = cur
                num = 0
        res += last_num
        return res

[BEST #3]
class Solution(object):
    def calculate(self, s):
        curr_op = "+"
        s += "+"
        
        temp = ""
        contain_digit = False
        stack = []
        for c in s:
            if c in "+-*/" and contain_digit:
                val = int(temp)
                temp = ""
                if curr_op == "+":
                    stack.append(val)
                elif curr_op == "-":
                    stack.append(-val)
                elif curr_op == "*":
                    a,b = stack.pop(), val
                    stack.append(a*b)
                else:
                    a,b = stack.pop(), val
                    sign = -1 if a*b < 0 else 1
                    stack.append(sign * (abs(a)/abs(b)))
                curr_op = c
            else:
                if c.isdigit():
                    contain_digit = True
                temp += c
                
        return sum(stack)
"""
class Solution(object):
    def calculate(self, s):
        stack = []
        
        i = 0
        
        val = 0
        cal = 0

        s = s.replace(" ", "")
        
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                if cal == 1:
                    while True:
                        if len(stack) == 0:
                            stack.append(val)
                            break
                        else:
                            tmp = stack.pop()
                        if tmp == '*':
                            val = int(stack.pop() * val)
                        elif tmp == '/':
                            val = int(stack.pop() / val)
                        else:
                            stack.append(tmp)
                            stack.append(val)
                            break
                else:
                    stack.append(val)
                stack.append(s[i])
                val = cal = 0
            elif s[i] == '*' or s[i] == '/':
                if cal == 1:
                    while True:
                        if len(stack) == 0:
                            stack.append(val)
                            break
                        else:
                            tmp = stack.pop()
                        if tmp == '*':
                            val = int(stack.pop() * val)
                        elif tmp == '/':
                            val = int(stack.pop() / val)
                        else:
                            stack.append(tmp)
                            stack.append(val)
                            break
                else:
                    stack.append(val)
                stack.append(s[i])
                cal = 1
                val = 0
            else:
                val = val*10 + ord(s[i]) - ord('0')
            i += 1

        if cal == 1:
            while True:
                if len(stack) == 0:
                    stack.append(val)
                    break
                else:
                    tmp = stack.pop()
                if tmp == '*':
                    val = int(stack.pop() * val)
                elif tmp == '/':
                    val = int(stack.pop() / val)
                else:
                    stack.append(tmp)
                    stack.append(val)
                    break
        else:
            stack.append(val)

        result = 0

        while len(stack) > 0:
            tmp = stack.pop(0)
            if tmp == '+':
                result = result + stack.pop(0)
            elif tmp == '-':
                result = result - stack.pop(0)
            else:
                result = tmp

        return result
        
if __name__ == '__main__':
    s = Solution()
    print(s.calculate("1+2*5/3+6/4*2"))
    print(s.calculate("14/3*2"))
    print(s.calculate("2*3+4"))
    print(s.calculate("3+3*3/3"))
    print(s.calculate(" 3/2 "))
    print(s.calculate(" 1-1+1 "))
    print(s.calculate("0-2147483647"))