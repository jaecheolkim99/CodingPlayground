"""
https://leetcode.com/submissions/detail/416145373/?from=/explore/featured/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3517/

[BEST]
class Solution(object):
    def insertionSortList(self, head):
        if not head: return
        
        temp = []
        curr = head
        while curr:
          temp.append(curr.val)
          curr = curr.next
          
        temp.sort()
        curr = head
        for val in temp:
          curr.val = val
          curr = curr.next
          
        return head

"""
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(-sys.maxint)
        
        node = head
        
        while node:
            next = node.next
            prev = dummy
            
            while prev.next and node.val > prev.next.val:
                prev = prev.next
                
            node.next = prev.next
            prev.next = node
            node = next
        
        return dummy.next
