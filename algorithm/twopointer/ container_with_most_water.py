"""11. Container With Most Water
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum area of water a container can hold, given a list of
        non-negative integers where each represents the height of a vertical
        line drawn at that index. The container is formed by any two lines
        and the x-axis; area = width * min(height of the two lines).

        Approach: two-pointer / greedy.
        Start with the widest possible container (leftmost and rightmost
        lines). At each step, the width can only shrink, so the only way
        to potentially find a larger area is to increase the limiting
        height. Move the pointer at the shorter line inward, since moving
        the taller one can never increase the area (width shrinks, height
        stays capped by the shorter line either way).

        Args:
            height: List of non-negative integers representing line heights.

        Returns:
            The maximum area (int) obtainable.

        Time complexity: O(n) — each pointer moves at most n times total.
        Space complexity: O(1).
        """
        result = -math.inf
        l, r = 0, len(height) - 1

        while l < r:
            curr_area = (r - l) * min(height[r], height[l])
            if curr_area > result:
                result = curr_area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return result

sol = Solution()

# Example 1: classic LeetCode example, expected output 49
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height1))  # 49