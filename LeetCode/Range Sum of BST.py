"""
https://leetcode.com/submissions/detail/420477979/?from=/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3532/

[BEST]
class Solution(object):
    def rangeSumBST(self, root, L, R):
        return self.bst_helper(root, L, R, 0)
    
    
    def bst_helper(self, root, L, R, sum_so_far):
        if not root:
            return sum_so_far
        if root.val<L:
            return self.bst_helper(root.right, L, R, sum_so_far)
        if root.val>R:
            return self.bst_helper(root.left, L, R, sum_so_far)
        sum_so_far+=root.val
        sum_so_far = self.bst_helper(root.left, L, R, sum_so_far)
        return self.bst_helper(root.right, L, R, sum_so_far)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorder(self, node, result, low, high):
        if node == None:
            return

        if node.val >= low and node.val <= high:
            result.append(node.val)
            self.inorder(node.left, result, low, high)
            self.inorder(node.right, result, low, high)
        elif node.val < low:
            self.inorder(node.right, result, low, high)
        elif node.val > high:
            self.inorder(node.left, result, low, high)
        return

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        result = []

        self.inorder(root, result, low, high)

        return sum(result)

if __name__ == '__main__':
    s = Solution()
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    root = TreeNode(1, left=t2, right=t3)

    print(s.rangeSumBST(root, 0, 5))