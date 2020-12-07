"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556/

class Solution(object):
    def connect(self, root):
        if (not root):
            return root
        
        q0 = collections.deque()
        q1 = collections.deque()
        q0.append(root)

        while len(q0) != 0:
            prev = None
            while len(q0) != 0:
                n = q0.popleft()
                n.next = prev
                prev = n
                if (n.right):
                    q1.append(n.right)
                if (n.left):
                    q1.append(n.left)                
            q0, q1 = q1, q0
        
        return root

"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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

if __name__ == '__main__':

    n1 = Node(1)
    n3 = Node(3)
    n2 = Node(2, left=n1, right=n3)

    s = Solution()
    s.connect(n2)