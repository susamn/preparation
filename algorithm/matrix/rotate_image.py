"""
48. Rotate Image
Solved
Medium
Topics
premium lock icon
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix), len(matrix[0])

        # Transpose
        for i in range(r):
            for j in range(i, c): # Very easy to make mistake to do range(c), but that will replace two times
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        for i in range(r):
            l,r = 0, len(matrix[0]) -1
            while l<r:
                matrix[i][l],matrix[i][r] = matrix[i][r], matrix[i][l]
                l +=1 
                r -= 1

        return matrix


soln = Solution()
print(soln.rotate([[1,2,3],[4,5,6],[7,8,9]]))

'''
The way to remember it rather than memorize it:

Transpose alone = reflect across the main diagonal (top-left to bottom-right).
A reflection across the diagonal + a reflection across a vertical or horizontal axis = a 90° rotation, and which axis you reflect across determines the direction.
Think of it as: rotate 90° CW = flip across "" diagonal, then flip left-right.
rotate 90° CCW = flip across "" diagonal, then flip up-down (or equivalently flip up-down then transpose).
180° = flip left-right AND up-down (no diagonal flip at all — it's just a point reflection).

'''