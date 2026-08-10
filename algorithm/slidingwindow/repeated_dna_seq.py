"""187. Repeated DNA Sequences
Medium
Topics
premium lock icon
Companies
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l,r=0,10
        res = {1:[],2:[]}
        while r<len(s):
            ss = s[l:r]
            if ss in res[1]:
                res[1].remove(ss)
                res[2].append(ss)
            else:
                res[1].append(ss)
            r += 1
            l += 1

        return res[2]


soln = Solution()
print(soln.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))