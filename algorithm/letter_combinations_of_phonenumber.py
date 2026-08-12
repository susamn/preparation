"""17. Letter Combinations of a Phone Number
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2:'abc', 3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        parts = [mapping[int(x)] for x in digits]
        result = []
        max_len = len(parts)

        def backtrack(index, current):
            if len(current) == max_len:
                result.append("".join(current))
                return
            
            for ch in parts[index]:
                current.append(ch)
                backtrack(index+1, current)
                current.pop()
        backtrack(0,[])
        return result

soln = Solution()
print(soln.letterCombinations("23"))
print(soln.letterCombinations("89"))
print(soln.letterCombinations("789"))