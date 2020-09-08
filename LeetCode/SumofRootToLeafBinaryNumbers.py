"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

[BEST]
class Solution(object):
    def sumRootToLeaf(self, root):
        if not root:
            return None
         
        if not root.left and not root.right:
            return root.val
        
        
        return self.evaluateSum(root, 0)
    
    def evaluateSum(self, root, total_sum):
        
        if not root.left and not root.right:
            return total_sum*2 + root.val
        
        elif not root.left:
            return self.evaluateSum( root.right, total_sum*2 + root.val )
            
        elif not root.right:
            return self.evaluateSum( root.left, total_sum*2 + root.val )
            
        else:
            return self.evaluateSum( root.right, total_sum*2 + root.val ) + \
                   self.evaluateSum( root.left, total_sum*2 + root.val )
"""

# Definition for a binary tree node.
class Solution(object):
    def sumRootToLeafWithSum(self, root, sum):
        if not root:
            return 0

        sum = sum * 2 + root.val

        if not root.left and not root.right:
            return sum

        return self.sumRootToLeafWithSum(root.left, sum) + self.sumRootToLeafWithSum(root.right, sum)
        
    def sumRootToLeaf(self, root):
        return self.sumRootToLeafWithSum(root, 0) 

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root_left = TreeNode(0)
    root_right = TreeNode(1)

    root_left_left = TreeNode(0)
    root_left_right = TreeNode(1)

    root_right_left = TreeNode(0)
    root_right_right = TreeNode(1)

    root.left = root_left
    root.right = root_right

    root_left.left = root_left_left
    root_left_right = root_left_right

    root_right.left = root_right_left
    root_right.right = root_right_right

    print(s.sumRootToLeaf(root))