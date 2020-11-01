"""
https://leetcode.com/submissions/detail/415525417/?from=/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3516/

[BEST]
class Solution(object):
    def getDecimalValue(self, head):
        numbaz = []
        total = 0
        while head:
            numbaz.append(head.val)
            head = head.next
        numbaz.reverse()
        for x in range(len(numbaz)):
            if numbaz[x] == 1:
                total = total + (2 ** x)
        return total

"""
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        result = 0

        while head:
            result = (result << 1)
            result += head.val
            head = head.next

        return result


if __name__ == '__main__':
    s = Solution()

    lst1 = ListNode(1)
    lst2 = ListNode(0, next = lst1)
    lst3 = ListNode(1, next = lst2)

    s.getDecimalValue(lst3)