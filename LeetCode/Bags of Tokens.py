"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3506/

[BEST]
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        # https://www.cnblogs.com/grandyang/p/13092555.html
        # greedy
        
        tokens.sort()
        score = 0
        res = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if P >= tokens[l]:
                score += 1
                P -= tokens[l]
                l += 1
            elif score:
                score -= 1
                P += tokens[r]
                r -= 1
            else:
                break
            res = max(res, score)
        return res
"""
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """        
        tokenlen = len(tokens)
        
        if tokenlen == 0:
            return 0
        
        tokens = sorted(tokens)
        
        if tokens[0] > P:
            return 0
        
        score = 0
        left = 0
        right = tokenlen - 1
        
        while (left <= right):
            if (P >= tokens[left]):
                score += 1
                P -= tokens[left]
                left += 1
            else:
                if right > left:
                    score -= 1
                    P += tokens[right]
                    right -= 1
                else:
                    break
        
        return score