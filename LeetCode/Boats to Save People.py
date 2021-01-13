"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602

[BEST]
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: 
                j -= 1
            i += 1
        return i
"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        result = 0

        while len(people) > 0:
            if len(people) > 1:
                if people.pop() + people[0] <= limit:
                    people.pop(0)
            else:
                people.pop()
            result += 1
        return result

if __name__ == "__main__":
    s = Solution()
    s.numRescueBoats([1,3,5,7,3,1], 7)