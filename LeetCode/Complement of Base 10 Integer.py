"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3484/

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

EXAMPLE:
Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

[BEST]
class Solution(object):
    def bitwiseComplement(self, N):
        binary = bin(N)
        binary = binary[2:]
        binary = list(binary)
        
        for i in range(len(binary)):
            if binary[i] == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'
        
       
        return int(''.join(binary),2)

"""
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        bitwise_comp = []

        while True:
            if N % 2 == 0:
                bitwise_comp.append(1)
            else:
                bitwise_comp.append(0)

            if N != 0:
                N = (int)(N / 2)
            else:
                if len(bitwise_comp) != 1 and bitwise_comp[-1] == 1:
                    bitwise_comp.pop()
                break

        while len(bitwise_comp) != 0:
            result = result * 2 + bitwise_comp.pop()

        return result

if __name__ == '__main__':
    s = Solution()

    print(s.bitwiseComplement(0))
