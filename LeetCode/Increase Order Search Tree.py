"""

[BEST]
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.inOrder(root)
        if not res:
            return 
        dummy = TreeNode(-1)
        cur = dummy
        for node in res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    
    def inOrder(self, root):
        if not root:
            return []
        res = []
        res.extend(self.inOrder(root.left))
        res.append(root)
        res.extend(self.inOrder(root.right))
        return res

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createOnlyRIghtChild(self, lst):
        if len(lst) != 1:            
            for i in range(len(lst)-1):
                node = lst[i]
                node.left = None
                node.right = lst[i+1]
            node.right.left = None
            node.right.right = None

    def inorder(self, root, result):

        if not root:
            return

        tmp = self.inorder(root.left, result)
        if tmp:
            result.append(tmp)
        result.append(root)
        tmp = self.inorder(root.right, result)
        if tmp:
            result.append(tmp)

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        result = []

        self.inorder(root, result)
        self.createOnlyRIghtChild(result)
        
        return result[0]