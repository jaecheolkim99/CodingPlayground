"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/

[BEST]
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        self.ans = None
        self.max_depth = 0
        def postorder(root, depth = 0):
            if not root:
                return depth
            
            l = postorder(root.left, depth+1)
            r = postorder(root.right, depth+1)
            self.max_depth = max(self.max_depth, l, r)
            if l == r == self.max_depth:
                self.ans = root
            return max(l, r)
        
        postorder(root)
        return self.ans

"""
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.depth = -1
        self.result = None
        
        self.postDepth(root, 0)
        
        return self.result
    
    def postDepth(self, node, depth):
        if node == None:
            return depth
        
        left = self.postDepth(node.left, depth + 1)
        right = self.postDepth(node.right, depth + 1)
        
        if left == right:
            self.depth = max(self.depth, left)
            if self.depth == left:
                self.result = node
        
        return max(left, right)
