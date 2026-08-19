"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2 & 3: If pivot found, find the successor to swap with
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at i + 1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 7, 4],        # Standard ascending -> [1, 3, 2]
        [3, 2, 1],        # Monotonically decreasing -> [1, 2, 3] (wraps around)
        [1, 1, 5],        # Duplicates present -> [1, 5, 1]
        [1, 5, 8, 4, 7, 6, 5, 3, 1], # Pivot in middle -> [1, 5, 8, 5, 1, 3, 4, 6, 7]
        [1],              # Single element -> [1]
        [2, 2, 2],        # All duplicates -> [2, 2, 2]
    ]

    soln = Solution()
    for original in test_cases:
        arr = list(original)
        soln.nextPermutation(arr)
        print(f"Input:  {original}")
        print(f"Output: {arr}\n")