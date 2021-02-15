"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/

[BEST]
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        for i in mat:
            res.append(sum(i))
        res=sorted([[y,x] for x,y in list(enumerate(res))])
        return [y for x,y in res[:k]]

"""
from collections import Counter
import operator

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        result = {}
        
        for row in range(len(mat)):
            counter = Counter(mat[row])
            result[row] = counter[1]

        #sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
        sorted_result = sorted(result.items(), key=operator.itemgetter(1))        

        lst = []
        cnt = 1

        for key in sorted_result:
            lst.append(key[0])
            if cnt == k:
                break
            cnt += 1
        return lst