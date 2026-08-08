"""
542. 01 Matrix
Medium
Topics
premium lock icon
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

from collections import deque

def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    
    # Step 1: Initialize
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = float('inf')  # mark unvisited
    
    # Directions
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Step 2: BFS
    while q:
        x, y = q.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n:
                if mat[nx][ny] > mat[x][y] + 1:
                    mat[nx][ny] = mat[x][y] + 1
                    q.append((nx, ny))
    
    return mat


assert updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]] 


'''
This is the classic multi-source BFS problem. The key insight: instead of running BFS from every 1, run BFS once from all 0s simultaneously.

🔑 Intuition
All 0s are sources (distance = 0)
Expand outward using BFS
First time you reach a 1 → that’s its shortest distance to a 0

Why it works:

BFS guarantees shortest path in an unweighted grid
Starting from all 0s avoids redundant work
'''

# BFS
# Time: O(m*n) - Each cell is processed at most once
# Space: O(m*n) - In worst case, all cells are 0s and are added to the queue