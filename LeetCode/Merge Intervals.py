"""
https://leetcode.com/submissions/detail/421671894/?from=/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3535/

[BEST]
class Solution(object):
    def merge(self, intervals):
        answer = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        rangeMin = intervals[0][0]
        rangeMax = intervals[0][1]
        for ele in intervals:

            if ele[0] > rangeMax:
                answer.append([rangeMin, rangeMax])
                rangeMin = ele[0]
                rangeMax = ele[1]

            if ele[0] < rangeMin:
                rangeMin = ele[0]
            if ele[1] > rangeMax:
                rangeMax = ele[1]

        answer.append([rangeMin, rangeMax])
        return answer
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = []
        current = intervals[0]
        result.append(current)

        for interval in intervals:
            current_start = current[0]
            current_end = current[1]
            interval_start = interval[0]
            interval_end = interval[1]

            if current_end >= interval_start:
                current[1] = max(current_end, interval_end)
            else:
                current = interval
                result.append(current)

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))

