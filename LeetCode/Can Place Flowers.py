"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

[BEST]
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
       
        if n <= 0:
            return True
        
        index = 0
        
        while (index < len(flowerbed)):
            if flowerbed[index]:
                index += 2
            else:
                if index < len(flowerbed) - 1 and flowerbed[index + 1]:
                    index += 3
                else:
                    n -= 1
                    index += 2
                    if n <= 0:
                        return True
        
        return n <= 0

"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """       

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                i += 2
            if n <= 0:
                return True
        return False