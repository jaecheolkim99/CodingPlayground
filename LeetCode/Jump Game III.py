"""
https://leetcode.com/submissions/detail/425350585/?from=/explore/challenge/card/november-leetcoding-challenge/568/week-5-november-29th-november-30th/3548/

[BEST]
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q = deque([start])
        while q:
            cur = q.popleft()
            if arr[cur]==0:
                return True
            if arr[cur]<0:
                continue
                
            for i in [cur-arr[cur], cur+arr[cur]]:
                if 0<=i<len(arr):
                    q.append(i)
            arr[cur] = -1

        return False       
"""
class Solution(object):

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        self.canreach = False
        self.visited = [False] * len(arr)
        maxlen = len(arr)

        result = self.search(arr, start, maxlen)
        return result

    def search(self, arr, start, maxlen):
        if arr[start] == 0:
            return True

        if self.visited[start] == True:
            return False

        self.visited[start] = True
        var = arr[start]
        ret = False

        if start + var < maxlen:
            ret = self.search(arr, start+var, maxlen)
            self.visited[start+var] = False
        if ret == False and start - var >= 0:
            ret = self.search( arr, start-var, maxlen)
            self.visited[start-var] = False
        return ret