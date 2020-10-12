"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492/

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


[BEST]
class Solution(object):
    def buddyStrings(self, A, B):
        len_a = len(A)
        len_b = len(B)
        if len_a != len_b: return False
        if A == B: return len_a > len(set(A))
        else:
            diff = []
            for a, b in zip(A, B):
                if a != b:
                    diff.append((a, b))
                    if len(diff) > 2: return False
            return len(diff) == 2 and diff[0] == diff[1][::-1]

"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        col_A = collections.Counter(A)
        col_B = collections.Counter(B)

        if col_A == col_B:
            diff = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    diff += 1
            if diff == 2:
                return True
            elif diff == 0:
                for k,v in col_A.items():
                    if v > 1:
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.buddyStrings("ab", "ba")
    s.buddyStrings("ab", "aa")
    s.buddyStrings("ab", "ab")

