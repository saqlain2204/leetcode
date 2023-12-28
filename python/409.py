'''
409 - Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
            Args: s (str): string of lowercase and/or uppercase English letters only
            Returns: int: length of longest palindrome that can be built with the letters in s
        '''
        char_freq = Counter(s)
        p_length = 0
        for i in char_freq.values():
            if i % 2 == 0:
                p_length += i

            else:
                p_length += i - 1

        return p_length if len(s) == p_length else p_length + 1

        
'''
Costraints:
1 <= s.length <= 2000
s consist of lowercase and/or uppercase English letters only.

Testcases:
"abccccdd" -> 7
"a" -> 1

'''
print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("a"))