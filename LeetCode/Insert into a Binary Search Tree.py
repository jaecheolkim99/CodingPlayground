"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3485/

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

[BEST]
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            node = TreeNode(val)
            return node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        root = self.insertVal(root, val)
        return root

    def insertVal(self, node, val):
        if node is None:
            node = TreeNode(val)
        else:
            if node.val > val:
                node.left = self.insertVal(node.left, val)
            else:
                node.right = self.insertVal(node.right, val)
        return node
