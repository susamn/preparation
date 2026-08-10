"""54. Spiral Matrix
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []

        while l <= r and u <= d:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1

            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1

            if u <= d:
                for i in range(r, l - 1, -1):
                    res.append(matrix[d][i])
                d -= 1

            if l <= r:
                for i in range(d, u - 1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res

soln = Solution()
print(soln.spiralOrder([[1,3,5,7],[10,11,16,20],[23,30,34,60]]))