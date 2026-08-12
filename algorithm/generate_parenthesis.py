"""
22. Generate Parentheses
Solved
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of n pairs of well-formed parentheses.

        Approach: backtracking, building the string one character at a time.
        Track:
          op = number of '(' placed so far
          cl = number of ')' placed so far

        A string of parentheses is "well-formed" at every prefix if and only if,
        reading left to right, the count of ')' never exceeds the count of '('.
        We enforce that invariant directly instead of generating all strings
        and filtering, which avoids exponential waste.
        """
        result = []
        st = []

        def backtrack(op, cl, n):
            # Base case: used all n opens and n closes -> valid combination complete
            if op == cl == n:
                result.append("".join(st))
                return

            # Condition 1: we may add '(' as long as we haven't used all n yet.
            # No upper-bound risk here since '(' never breaks well-formedness.
            if op < n:
                st.append("(")
                backtrack(op + 1, cl, n)
                st.pop()  # undo the choice before trying the next branch

            # Condition 2: we may add ')' only if op > cl.
            # This is the key correctness constraint: if we added ')' when
            # cl >= op, we'd have more closes than opens at this point in the
            # string, producing something like ")(" — invalid. Requiring
            # op > cl guarantees there's an unmatched '(' available to close.
            if op > cl:
                st.append(")")
                backtrack(op, cl + 1, n)
                st.pop()

        backtrack(0, 0, n)
        return result

sol = Solution()
output = sol.generateParenthesis(3)
print(output)