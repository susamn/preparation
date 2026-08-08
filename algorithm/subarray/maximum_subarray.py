"""
53. Maximum Subarray

Given an integer array nums of length n, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= n <= 10^5
-10^4 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


def maxSubArray(nums: list[int]) -> int:
    max_so_far = float('-inf')
    current_max = 0
    for num in nums:
        current_max += num
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
    return max_so_far


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))