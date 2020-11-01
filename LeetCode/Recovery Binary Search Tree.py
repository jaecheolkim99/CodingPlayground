"""
https://leetcode.com/submissions/detail/415546486/?from=/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3514/

[BEST]
class Solution(object):
    # good explaination by tushar roy on morris inorder (it takes only o(1) space)
    # https://www.youtube.com/watch?v=wGXB9OWhPTg&ab_channel=TusharRoy-CodingMadeSimple
    # morris inorder does not need true_pred, we use true_pred to keep a track of true pred  
    def recoverTree(self, root):        
        if not root: return []
        
        x = y = true_pred = pred = None
        curr = root

        while curr:
            if curr.left == None:
                # check if swapped elements
                if true_pred and curr.val < true_pred.val:
                    y = curr
                    if x is None:
                        x = true_pred 
                # save true pred, before changing its value
                true_pred = curr
                curr = curr.right
            else:
                pred = curr.left
                # keep moving to the right most element of the left of current
                while pred.right != None and pred.right != curr:
                    pred = pred.right

                if pred.right == None:
                    pred.right = curr
                    curr = curr.left                    
                elif pred.right == curr:
                    # check if swapped elements
                    if true_pred and curr.val < true_pred.val:
                        y = curr
                        if x is None:
                            x = true_pred 
                    # save true pred, before changing its value
                    true_pred = curr
                    pred.right = None
                    curr = curr.right
        
        x.val, y.val = y.val, x.val

"""
class Solution(object):
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)

        if self.prev == None:
            self.prev = node
        else:
            if node.val < self.prev.val:
                if self.left == None:
                    self.left = self.prev
                self.right = node
            self.prev = node

        self.inorder(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.left = None
        self.right = None
        self.prev = None

        self.inorder(root)
        if self.right != None and self.left != None:
            val = self.right.val
            self.right.val = self.left.val
            self.left.val = val