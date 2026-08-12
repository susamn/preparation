"""236. Lowest Common Ancestor of a Binary Tree
Solved
Medium
Topics
premium lock icon
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: hit a null node, or found p or q -> return it up
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found in different subtrees -> current root is the LCA
        if left and right:
            return root

        # otherwise, propagate up whichever side found something
        # (or None if neither side found anything)
        return left if left else right

'''
Approach:

- Recurse down the tree. At each node, ask: "is p or q in my left subtree? in my right subtree?"
- Base case: if root is None (dead end) or root itself is p or q, return root immediately — this handles both "found the target" and "a node can be its own ancestor" (Example 2).
- If both the left and right recursive calls return non-None, that means p and q were found in different subtrees of the current node — so this node is exactly where their paths diverge, making it the LCA. Return root.
- If only one side returned something, that means both p and q (or just one of them, at this point in the recursion) live entirely within that one subtree, so pass that result upward unchanged.
- If neither side found anything, return None.
'''

sol = Solution()

# tree = [3,5,1,6,2,0,8,null,null,7,4]
#             3
#           /   \
#          5     1
#         / \   / \
#        6   2 0   8
#           / \
#          7   4
n7 = TreeNode(7)
n4 = TreeNode(4)
n6 = TreeNode(6)
n2 = TreeNode(2, n7, n4)
n0 = TreeNode(0)
n8 = TreeNode(8)
n5 = TreeNode(5, n6, n2)
n1 = TreeNode(1, n0, n8)
root = TreeNode(3, n5, n1)

result = sol.lowestCommonAncestor(root, n5, n1)
print(f"LCA(5, 1) = {result.val}  (expected 3)")

result = sol.lowestCommonAncestor(root, n5, n4)
print(f"LCA(5, 4) = {result.val}  (expected 5)")

result = sol.lowestCommonAncestor(root, n7, n4)
print(f"LCA(7, 4) = {result.val}  (expected 2)")