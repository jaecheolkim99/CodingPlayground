"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
[BEST]
ss Solution(object):
    def addOneRow(self, root, v, d):
        queue = list()
        queue.append(root)        
        count = 1        
        height = 1        
        if d == 1:
            demo_root = TreeNode(v)            
            demo_root.left = root            
            return demo_root
        temp_right = None        
        temp_left = None
        while queue:            
            step = 0            
            no_of_member = 0            
            reached_depth = True if height == d - 1 else False
                
            while step < count:
                node = queue.pop(0)
                step += 1
                temp_right = node.right
                temp_left = node.left
                
                if reached_depth:
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = temp_left
                    node.right.right = temp_right
                    continue
                
                if temp_left:
                    queue.append(temp_left)
                    no_of_member += 1
                    
                if temp_right:
                    queue.append(temp_right)
                    no_of_member += 1
                                         
            height += 1
            count = no_of_member        
        return root
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v, left=root)
            return node
        
        stack = [root]
        depth = 1
        
        while stack:
            if depth+1 == d:
                while stack:
                    popnode = stack.pop()
                    lnode = TreeNode(v, left=popnode.left)
                    popnode.left = lnode
                    rnode = TreeNode(v, right=popnode.right)
                    popnode.right = rnode
                break
            depth += 1
            nstack = []
            while stack:
                popnode = stack.pop()
                if popnode.left:
                    nstack.append(popnode.left)
                if popnode.right:
                    nstack.append(popnode.right)                
            stack = nstack
        
        return root