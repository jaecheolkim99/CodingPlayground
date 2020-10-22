"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3504/

[BEST]
class Solution(object):
    def minDepth(self,root): 
        # Corner Case.Should never be hit unless the code is  
        # called on root = NULL 
        if root is None: 
            return 0 

        # If left subtree is Null, recur for right subtree 
        if root.left is None: 
            return self.minDepth(root.right)+1

        # If right subtree is Null , recur for left subtree 
        if root.right is None: 
            return self.minDepth(root.left) +1 

        return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1) 
"""
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        if root == None:
            return 0

        queue = collections.deque()
        queue.append({root:1})

        while(len(queue) > 0):
            item = queue.popleft()

            for elem in item:
                if elem.left == None and elem.right == None:
                    return item[elem]

                if elem.left != None:
                    queue.append({elem.left:item[elem]+1})

                if elem.right != None:
                    queue.append({elem.right:item[elem]+1})

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    s = Solution()
    print(s.minDepth(root))