"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600/

[BEST]
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        ### i is pointer of nums1 and j is pointer of nums2 ###
        i, j = 0, 0
        nums1_copy = nums1[:]
        nums1[:] = []
        
        ### add the smallest one in num2 or num1_copy into nums1 ###
        while i<m and j<n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        
        ### if there are still elements to add ###
        while i < m:
            nums1.append(nums1_copy[i])
            i+=1

        while j < n:
            nums1.append(nums2[j])
            j += 1

"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        origin = m + n

        while i + j < m + n:
            if i == m:
                while len(nums1) != i:
                    nums1.pop()
                nums1.append(nums2[j])
                j += 1
                i += 1
                m += 1
            elif j == n:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                m += 1
            else:
                i += 1

        while len(nums1) != origin:
            nums1.pop()

        return nums1


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(s.merge([2,0], 1, [1], 1))