"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3473/

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. 
Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, 
and makes Ashe be in poisoned condition immediately.

"""
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        start = 0
        end = 0
        result = 0
        
        for i in range(len(timeSeries)):
            if timeSeries[i] >= end:
                result += duration
            else:
                result += timeSeries[i] - start
            
            start = timeSeries[i]
            end = start + duration
        
        return result