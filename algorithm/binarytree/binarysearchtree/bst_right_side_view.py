"""
199. Binary Tree Right Side View
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List, Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            length = len(q)
            for i in range(length):
                elem = q.popleft()
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
                if i == length - 1:
                    result.append(elem.val)  # last node in this level = rightmost
        return result

soln = Solution()
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))) 
print(soln.rightSideView(root)) #Expected output: [1, 3, 4]