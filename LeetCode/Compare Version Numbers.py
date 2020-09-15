"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1; otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. For example,
version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.

[BEST]
class Solution(object):
    def compareVersion(self, version1, version2):
        l1 = [int(i) for i in version1.split('.')]
        l2 = [int(i) for i in version2.split('.')]
        i = len(l2) - 1
        while i >= 0:
            if l2[i]:
                break
            l2 = l2[:-1]
            i -= 1
        i = len(l1) - 1
        while i >= 0:
            if l1[i]:
                break
            l1 = l1[:-1]
            i -= 1
        for i in range(min(len(l2), len(l1))):
            if l1[i] < l2[i]:
                return -1
            elif l2[i] < l1[i]:
                return 1
        
        if len(l1) > len(l2):
            return 1
        elif len(l2) > len(l1):
            return -1
        return 0
"""

class Solution(object):
    def checkZero(self, list_version, idx, max_idx, type):
        for i in range(idx, max_idx):
            if list_version[i] != 0:
                if type == 0:
                    return -1
                return 1
        return 0

    def convertListStrToInt(self, lst):
        intLst = []
        first_zero = 0
        for i in range(len(lst)):
            if int(lst[i]) != 0 and first_zero != 0:
                intLst.append(int(lst[i]))
            else:
                intLst.append(int(lst[i]))
                first_zero += 1
        return intLst

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s_ver1 = version1.split(".")
        s_ver2 = version2.split(".")

        s_ver1 = self.convertListStrToInt(s_ver1)
        s_ver2 = self.convertListStrToInt(s_ver2)

        len_ver1 = len(s_ver1)
        len_ver2 = len(s_ver2)

        max_len = max(len_ver1, len_ver2)

        for i in range(max_len):
            idx = i + 1
            if len_ver1 < idx:
                return self.checkZero(s_ver2, i, len_ver2, 0)
            if len_ver2 < idx:
                return self.checkZero(s_ver1, i, len_ver1, 1)
            if idx == len_ver1 and idx == len_ver2:
                if s_ver1[i] < s_ver2[i]:
                    return -1
                if s_ver1[i] > s_ver2[i]:
                    return 1
                return 0
            if s_ver1[i] < s_ver2[i]:
                return -1
            if s_ver1[i] > s_ver2[i]:
                return 1
