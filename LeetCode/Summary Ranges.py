"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510/

[BEST]
class Solution(object):
    def summaryRanges(self, nums):
        # we define a "range" to be a series of consecutive numbers
        # I think this is a candidate for the greedy algorithm. We can keep track of two indices and reset as necessary
        
        # can we assume that they are distinct? and that we can tell the difference between distinct ranges if the end of one range is more than 1 apart from the beginning of another?r?
        
        # [0,1,2,3] --> "0->3", [0,1,2,4], --> ["0->2", "4"], [0, 2, 7] --> ["0", "2", "7"]
        
        # handle end of list
        
        ranges = []
        
        if len(nums) < 1: 
            return ranges
        
        start_num = nums[0]
        prev_num = nums[0]
        
        for index in range(1, len(nums)):
            current_num = nums[index]
            difference = current_num - prev_num
            
            if difference > 1:
                if start_num == prev_num:
                    ranges.append(str(start_num))
                else:
                    ranges.append(str(start_num) + "->" + str(prev_num))
                start_num = current_num
                    
            prev_num = current_num
            
        # still need to account for last part of range when we run off list
        if start_num == prev_num:
            ranges.append(str(start_num))
        else:
            ranges.append(str(start_num) + "->" + str(prev_num))
            
        return ranges
"""
class Solution(object):
    def addString(self, start, end, result):
        delimiter = '->'

        if start == end:
            result.append(str(start))
        else:
            result.append(str(start)+delimiter+str(end))


    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        maxlen = len(nums)

        if maxlen == 0:
            return

        start = nums[0]
        conti = start
        result = []
        delimiter = '->'
        added = 0

        for i in range(maxlen):
            if nums[i] != start and conti != nums[i]:
                if nums[i] - 1 != conti:
                    self.addString(start, nums[i-1], result)
                else:
                    conti = nums[i]

                if i + 1 < maxlen:
                    if conti != nums[i]:
                        start = nums[i]
                        conti = start
                else:
                    if conti != nums[i]:
                        result.append(str(nums[i]))
                    else:
                        self.addString(start, nums[i], result)
            else:
                conti = nums[i]
                if i + 1 == maxlen:
                    if start != nums[i]:
                        self.addString(start, nums[i], result)
                    else:
                        result.append(str(nums[i]))

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([1,2,4,4,5]))
    print(s.summaryRanges([4, 4]))
    print(s.summaryRanges([0,1,2,4,5,7]))
    print(s.summaryRanges([0,2,3,4,6,8,9]))