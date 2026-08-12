"""
498. Diagonal Traverse

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""

from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverse a matrix in the zigzag diagonal order used by LeetCode 498:
        alternate diagonals go up-right then down-left.

        Key idea: every cell (r, c) lies on diagonal k = r + c. All cells on
        the same diagonal share the same k. Diagonals with even k are read
        bottom-left -> top-right; diagonals with odd k are read
        top-right -> bottom-left.

        IMPORTANT — this implementation builds each diagonal bucket by
        iterating COLUMN-WISE, not row-wise:

            for c in range(cols):       # outer loop: walk columns left to right
                for r in range(rows):   # inner loop: walk rows top to bottom

        For a fixed diagonal k, as the outer `c` increases, the matching
        `r = k - c` decreases. So within seq[k], entries are naturally
        appended in order of DECREASING row (equivalently, increasing
        column) — i.e. bottom-left -> top-right along that diagonal.
        That natural order is exactly what an even-k diagonal needs, so it's
        used as-is; an odd-k diagonal needs the opposite (top-right ->
        bottom-left), so it's reversed before being added to the result.

        If you instead looped row-wise (outer r, inner c), the natural
        append order within each bucket would be flipped, and the even/odd
        reversal logic below would need to be swapped too. Column-wise
        iteration + "reverse the odd diagonals" is the specific pairing that
        makes this implementation correct.
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)

        for c in range(cols):
            for r in range(rows):
                diagonals[c + r].append(matrix[r][c])

        result = []
        for k in sorted(diagonals.keys()):
            if k % 2 == 0:
                result.extend(diagonals[k])          # bottom-left -> top-right, natural order
            else:
                result.extend(reversed(diagonals[k]))  # top-right -> bottom-left, needs flip
        return result

sol = Solution()
print(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) 
print ("Expected: [1, 2, 4, 7, 5, 3, 6, 8, 9]")