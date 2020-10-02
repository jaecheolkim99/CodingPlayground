"""
https://leetcode.com/explore/featured/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

[Best]
class RecentCounter(object):

    def __init__(self):
        self.queue = collections.deque([])

    def ping(self, t):
        self.queue.append(t)
        while (t - 3000 > self.queue[0]):
            self.queue.popleft()
        return len(self.queue)


"""
class RecentCounter(object):

    def __init__(self):        
        self.lst = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.lst.append(t)

        result = 0
        t = t - 3000

        for i in range(len(self.lst)-1, -1, -1):
            if self.lst[i] < t:
                return result
            result += 1

        return result

if __name__ == '__main__':
    s = RecentCounter()
    print(s.ping(1))
    print(s.ping(100))
    print(s.ping(3001))
    print(s.ping(3002))