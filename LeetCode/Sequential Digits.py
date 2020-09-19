"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345] 
"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
        result = []
        candidate = 12
        digit = 2
        inc = 11
        
        while (candidate < high):
            check = candidate;
            
            for i in range(9-digit+1):
                if check > high:
                    return result
                if check >= low and check <= high:
                    result.append(check)            
                check += inc
            
            digit += 1
            candidate = candidate*10 + digit
            inc = inc * 10 + 1
                
        return result