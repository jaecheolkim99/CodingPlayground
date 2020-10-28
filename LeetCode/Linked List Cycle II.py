"""
https://leetcode.com/submissions/detail/413764275/?from=/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3509/

[BEST]
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                
                slow2 = head

                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next

                return slow

"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pos = head
        history = {}
        index = 0

        while(pos != None):
            if not pos in history:
                history[pos] = index
            else:
                return pos
            pos = pos.next
            index += 1

        return pos
