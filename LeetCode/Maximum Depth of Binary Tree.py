"""
https://leetcode.com/submissions/detail/426063970/?from=/explore/featured/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/

[BEST]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        Q=[(root,1)]
        depth=0
        while Q:
            cur=Q.pop(0)
            depth=cur[1]
            if cur[0].left:
                Q.append((cur[0].left,depth+1))
            if cur[0].right:
                Q.append((cur[0].right,depth+1))
        return depth

"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))