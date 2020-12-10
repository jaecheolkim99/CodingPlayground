"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        mod = [0] * 60
        count = 0
        for t in time:
            mod[t%60]+=1
        
        for i in range(31):
            if i == 0 or i==30:
                count+=mod[i]* (mod[i]-1) // 2
            else:
                count += mod[i] * mod[60-i]
        return count
"""
class Solution(object):
    def combinationHash(self, hash):
        if hash < 2:
            return 0
        return int(hash*(hash-1)/2)


    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        hash = [0]*60

        for i in range(len(time)):
            hash[int(time[i] % 60)] += 1
            #print(int(time[i] % 60))

        result = self.combinationHash(hash[0])

        for i in range(1, 30):
            result = result + int(hash[i] * hash[60-i])

        result = result + self.combinationHash(hash[30])

        return result

if __name__ == '__main__':
    s = Solution()
    #print(s.numPairsDivisibleBy60([30,20,150,100,40,60]))
    print(s.numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]))