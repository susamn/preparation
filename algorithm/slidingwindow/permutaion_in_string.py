"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        if s1_count == window_count:
            return True

        # Slide fixed window of size len(s1) across s2
        for r in range(len1, len2):
            # Add character entering window on right
            window_count[s2[r]] += 1
            
            # Remove character leaving window on left
            left_char = s2[r - len1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]  # Keep map size clean for comparison

            # O(26) == O(1) comparison
            if s1_count == window_count:
                return True

        return False

solver = Solution()

# Case 1: Permutation present ("ba" inside "eidbaooo") -> True
print(solver.checkInclusion("ab", "eidbaooo"))

# Case 2: Permutation not present -> False
print(solver.checkInclusion("ab", "eidboaoo"))

# Case 3: s1 longer than s2 -> False
print(solver.checkInclusion("hello", "hi"))

# Case 4: Exact match -> True
print(solver.checkInclusion("adc", "dcda"))