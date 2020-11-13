"""
https://leetcode.com/submissions/detail/420019346/?from=/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3529/

[BEST]
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        
        if not root.left:
            return root
        
        node = root
        while node.left:
            cur = node
            next = node.next
            
            node.left.next = node.right
            while next:
                cur.right.next = next.left
                next.left.next = next.right
                cur = next
                next = next.next
                
            node = node.left
            
        return root
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        nodes = [root] if root else []
        
        while nodes:
            nxt_nodes = []
            last = None
            for node in nodes:
                if last:
                    last.next = node
                if node.left:
                    nxt_nodes.append(node.left)
                if node.right:
                    nxt_nodes.append(node.right)
                last = node
            nodes = nxt_nodes
        return root