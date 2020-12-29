"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/

[BEST]
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        
        self.count = 0
        
        def search(node, digitcount):
            digitcount = digitcount ^ (1 << node.val)
            if node.left:
                search(node.left, digitcount)
            
            if node.right:
                search(node.right, digitcount)
                
            if not node.left and not node.right:
                if digitcount & (digitcount - 1) == 0:
                    self.count += 1
                return
        
        search(root, 0)
        
        return self.count

"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isPalindrom(self, lst):
        countinglst = [0]*10
        for i in range(len(lst)):
            countinglst[lst[i]] += 1

        oddcounter = 0

        for i in range(1, 10):
            if countinglst[i] % 2 == 1:
                oddcounter += 1
            if oddcounter > 1:
                return 0
        return 1

    def dfs(self, node, lst):
        if node.left == None and node.right == None:
            self.result += self.isPalindrom(lst)
        if node.left != None:
            lst.append(node.left.val)
            self.dfs(node.left, lst)
            lst.pop()
        if node.right != None:
            lst.append(node.right.val)
            self.dfs(node.right, lst)
            lst.pop()

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        self.result = 0
        lst = []
        lst.append(root.val)
        self.dfs(root, lst)
        return self.result

if __name__ == '__main__':
    lchild = TreeNode(3, left=TreeNode(3), right=TreeNode(1))
    rchild = TreeNode(1, right=TreeNode(1))
    root = TreeNode(2, left=lchild, right=rchild)

    s = Solution()
    print(s.pseudoPalindromicPaths(root))