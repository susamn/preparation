"""
670. Maximum Swap
Medium
Topics
premium lock icon
Companies
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        # last[d] = rightmost index where digit d occurs
        last = {int(d): i for i, d in enumerate(digits)}

        for i in range(n):
            cur = int(digits[i])
            for d in range(9, cur, -1):
                if last.get(d, -1) > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num

soln = Solution()
print(soln.maximumSwap(1296))