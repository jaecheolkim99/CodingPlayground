"""
https://leetcode.com/submissions/detail/426440762/?from=/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/

[BEST]
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.arr = []
        curr = head
        while curr:
            self.arr.append(curr.val)
            curr = curr.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return choice(self.arr)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self._head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        
        value = -1
        node, n = self._head, 0
        
        while node:
            value = node.val if randint(1, n+1) == 1 else value
            node = node.next
            n = n + 1
        return value