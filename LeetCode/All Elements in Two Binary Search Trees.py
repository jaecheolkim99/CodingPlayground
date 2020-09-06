"""
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

[example]
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
"""

"""
[BEST]
class Solution(object):
    def getAllElements(self, root1, root2):
        stack1,stack2,output = [],[],[]
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right
        return output
"""

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def InorderTraverse(node):
            if not node:
                return []
            return InorderTraverse(node.left) + [node.val] + InorderTraverse(node.right)

        return sorted(InorderTraverse(root1) + InorderTraverse(root2))

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)

    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)

    print(s.getAllElements(root, root2))