'''
1347. Minimum Number of Steps to Make Two Strings Anagram
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] * 26
        count_t = [0] * 26
        for i in s:
            count_s[ord(i) - ord('a')] += 1
        for i in t:
            count_t[ord(i) - ord('a')] += 1

        ans = 0
        for i in range(0,26):
            ans += abs(count_s[i] - count_t[i])
        return ans//2
    
'''
Constraints:
1 <= s.length <= 50000
s.length == t.length
s and t contain lowercase English letters only.

Test case:
"bab", "aba" -> 1
"leetcode", "practice" -> 5
"anagram", "mangaar" -> 0
'''

print(Solution().minSteps("bab", "aba"))
print(Solution().minSteps("leetcode", "practice"))
print(Solution().minSteps("anagram", "mangaar"))