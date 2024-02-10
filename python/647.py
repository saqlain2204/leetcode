'''
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
'''
class Solution:
    def check_pal(self, s: str, start: int, end: int) -> bool:
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if self.check_pal(s, i, j):
                    count += 1
            ans += count
        return ans

'''
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.

Test Cases:
Input: s = "abc"
Output: 3

Input: s = "aaa"
Output: 6
'''