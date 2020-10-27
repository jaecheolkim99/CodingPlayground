"""


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
