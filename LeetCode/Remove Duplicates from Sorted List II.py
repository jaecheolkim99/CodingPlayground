"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/

[BEST]
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = p1 = ListNode(val=None, next=head)
        p2 = head
        while p1 and p2:
            #print(p1.val, p2.val)
            p2 = p2.next
            removed = False
            while p1.next and p2 and p1.next.val == p2.val:
                p2 = p2.next
                removed = True
            if removed:
                p1.next = p2
            else:
                p1 = p1.next
        return dummyNode.next

"""
from collections import OrderedDict

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def makeList(self, odic):
        head = node = None

        for key, val in odic.items():
            if val == 1:
                if head == None:
                    head = node = ListNode(key)
                else:
                    node.next = ListNode(key)
                    node = node.next
        return head

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odic = OrderedDict()

        if head == None:
            return None

        while head:
            if head.val in odic:
                odic[head.val] = 0
            else:
                odic[head.val] = 1
            head = head.next

        return self.makeList(odic)


if __name__ == '__main__':
    s = Solution()

    n4 = ListNode(3)
    n3 = ListNode(3, next=n4)
    n2 = ListNode(2, next=n3)
    n1 = ListNode(1, next=n2)
    n0 = ListNode(0, next=n1)

    print(s.deleteDuplicates(n0))