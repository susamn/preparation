"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


def longestValidParentheses_Stack(s: str) -> int:
    stack = [-1]
    max_length = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

def longestValidParentheses_DP(s: str) -> int:
    n = len(s)
    dp = [0] * n
    max_len = 0

    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            else:
                prev = i - dp[i-1] - 1
                if prev >= 0 and s[prev] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[prev-1] if prev >= 1 else 0)
            max_len = max(max_len, dp[i])

    return max_len


if __name__=='__main__':
    print(longestValidParentheses_DP("(()"))
    print(longestValidParentheses_DP("))))))))()"))
    print(longestValidParentheses_DP(")()())"))
    print(longestValidParentheses_DP(""))
    print(longestValidParentheses_DP("()(()"))
    print(longestValidParentheses_DP("(()())"))
