"""
https://leetcode.com/submissions/detail/417689537/?from=/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/


[BEST]
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        length1 = self.getLength(l1)
        length2 = self.getLength(l2)
        
        if length1 > length2:
            pointer = self.getIthPointer(l1, length1 - length2 - 1)
            
            if self.sumLists(pointer.next, l2) == 1:
                if self.incrementDigit(l1, pointer) == 1:
                    head = ListNode()
                    head.val = 1
                    head.next = l1

                    return head
            return l1
            
        elif length1 < length2:
            pointer = self.getIthPointer(l2, length2 - length1 - 1)
            
            if self.sumLists(pointer.next, l1) == 1:
                if self.incrementDigit(l2, pointer) == 1:
                    head = ListNode()
                    head.val = 1
                    head.next = l2

                    return head
                
            return l2
                
        else:
            if self.sumLists(l1, l2) == 1:
                head = ListNode()
                head.val = 1
                head.next = l1
                
                return head
            else:
                return l1
            
    def incrementDigit(self, node, pointer):
        if node == pointer:
            node.val += 1
        else:
            node.val += self.incrementDigit(node.next, pointer)
        
        if node.val > 9:
            node.val -= 10
            return 1
        
        return 0
           
    def sumLists(self, l1, l2):
        if l1 is None:
            return 0
        
        l1.val += l2.val + self.sumLists(l1.next, l2.next)
        
        if l1.val > 9:
            l1.val -= 10
            return 1
        
        return 0
        
    def getIthPointer(self, head, n):
        current = head
        
        while n > 0:
            current = current.next
            n -= 1
            
        return current
        
    def getLength(self, head):
        current = head
        length = 0
        
        while current is not None:
            length += 1
            current = current.next
            
        return length

"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = l1
        s1 = []
        while cur:
            s1.append(cur.val)
            cur = cur.next

        cur = l2
        s2 = []
        while cur:
            s2.append(cur.val)
            cur = cur.next

        carry = 0
        v1 = 0
        v2 = 0
        NewNode = None

        while s1 or s2:
            if s1:
                v1 = s1.pop()
            else:
                v1 = 0
            if s2:
                v2 = s2.pop()
            else:
                v2 = 0

            sum = (carry + v1 + v2) % 10
            carry = int((carry + v1 + v2) / 10)

            NewNode = ListNode(sum, next=NewNode)

        if carry == 1:
            NewNode = ListNode(1, next=NewNode)

        return NewNode
