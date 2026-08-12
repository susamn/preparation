"""
1695. Maximum Erasure Value

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104

"""

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        You are given an array of positive integers nums and want to erase a
        subarray containing unique elements. The erasure score is the sum of
        removed elements. Return the maximum score you can get by erasing
        exactly one subarray.

        Approach: sliding window (two pointers) + running sum.
          l, r        -> left/right bounds of the current window [l, r]
          window      -> set of values currently inside the window,
                         used for O(1) "have we seen this value already" checks
          curr_val    -> running sum of the current window (avoids re-summing
                         on every iteration)
          result      -> best (max) window sum seen so far

        Invariant: at the top of each outer-loop iteration, [l, r) is a
        valid window containing only unique values (r itself hasn't been
        folded in yet for this iteration's shrink step).

        For each new right-pointer value nums[r]:
          1. Speculatively add it to curr_val.
          2. While that value is already present in the window, shrink from
             the left: subtract nums[l] from curr_val, remove it from the
             set, and advance l. This restores uniqueness before nums[r] is
             officially added to the window set.
          3. Add nums[r] to the window set, update the best result, advance r.
        """
        result = 0
        l = 0
        r = 0
        window = set()
        curr_val = 0

        while r < len(nums):
            val = nums[r]
            curr_val += val

            # Shrink the window from the left until val is no longer a duplicate
            while val in window:
                curr_val -= nums[l]
                window.remove(nums[l])
                l += 1

            window.add(val)
            result = max(result, curr_val)
            r += 1

        return result

sol = Solution()
result = sol.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
print(result) # Expected 8