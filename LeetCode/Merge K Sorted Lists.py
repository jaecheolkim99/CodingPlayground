"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

[BEST]
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        sorted_list = ListNode()
        head = sorted_list
        nums = []
        
        for list_node in lists:
            while list_node:
                nums.append(list_node.val)
                list_node = list_node.next
        
        nums.sort()
        
        
        for num in nums:
            sorted_list.next = ListNode(num)
            sorted_list = sorted_list.next
        
        
        return head.next
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        mlen = len(lists)

        if mlen == 0:
            return None
        if mlen == 1:
            return lists[0]

        rdata = []
        for list in lists:
            if list == None:
                continue
            while list:
                rdata.append(list.val)
                list = list.next

        if len(rdata) == 0:
            return None

        rdata.sort()
        head = ListNode(-1)
        node = head

        for i in range(len(rdata)):
            next = ListNode(rdata[i])
            node.next = next
            node = node.next

        return head.next