"""
https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3525/

=======================================================================================================
[Solution] : https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/solution/
=======================================================================================================
Approach #1: Recursion
=======================================================================================================
Let's start from Brute Force.

A typical Brute Force approach is to compare every node with its ancestors. 
In the worst case, we have to compare every node-pair (when the tree is a single line).

The time complexity would be O(N^2), given N is the number of nodes in the binary tree.

Can we simplify it?

Since the problem asks us the Maximum Difference, maybe we do not need to compare all ancestor for a given node and we only need to compare the ancestors with Maximum value and Minimum value.
Therefore, for a given node, we only need the maximum value and the minimum value from the root to this node.
To achieve this, we can define a function helper to start recursion, which receives a node and two integers, the maximum and minimum value of its ancestors, as input.
In the function helper, we need to update the maximum difference, the current maximum value, and the current minimum value.

Algorithm
Step 1: Initialize a variable result to record the required maximum difference.
Step 2: Define a function helper, which takes three arguments as input.
        The first argument is the current node, and the second and third arguments are the maximum and minimum values along the root to the current node, respectively.
        In the function helper, update result and call helper on the left and right subtrees.

Step 3: Run helper on the root. It will automatically do recursion on every node.
Step 4: Finally, return result.

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result

Complexity Analysis
Let N be the number of nodes in the binary tree.

Time complexity: O(N) since we visit all nodes once.
Space complexity: O(N) since we need stacks to do recursion, and the maximum depth of the recursion is the height of the tree, which is O(N) in the worst case and O(log(N)) in the best case.

=======================================================================================================
Approach #2: Maximum Minus Minimum
=======================================================================================================
An insight is that:

Given any two nodes on the same root-to-leaf path, they must have the required ancestor relationship.

Therefore, we just need to record the maximum and minimum values of all root-to-leaf paths and return the maximum difference.
To achieve this, we can record the maximum and minimum values during the recursion and return the difference when encountering leaves.

Algorithm
Step 1: Define a function helper, which takes three arguments as input and returns an integer.
 - The first argument node is the current node, and the second argument cur_max and third argument cur_min are the maximum and minimum values along the root to the current node, respectively.
 - Function helper returns cur_max - cur_min when encountering leaves. Otherwise, it calls helper on the left and right subtrees and returns their maximum.

Step 2: Run helper on the root and return the result.

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)

Complexity Analysis
Let N be the number of nodes in the binary tree.

Time complexity: O(N) since we visit all nodes once.
Space complexity: O(N) since we need stacks to do recursion, and the maximum depth of the recursion is the height of the tree, which is O(N) in the worst case and O(log(N)) in the best case.
"""