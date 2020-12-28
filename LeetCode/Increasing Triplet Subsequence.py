"""

[TEST]


"""
class Solution(object):
    def increasingTriplet(self, nums):
        smallest, biggest = sys.maxint, sys.maxint
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= biggest:
                biggest = num
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.increasingTriplet([2,1,5,0,4,6])