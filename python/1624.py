'''
1624. Largest Substring Between Two Equal Characters
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
'''

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                if i != j and s[i] == s[j]:
                    ans = max(ans, (j - i) - 1)
        return ans

'''
Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.

Testcases:
"aa" -> 0
"abca" -> 2
"cbzxy" -> -1
"cabbac" -> 4
'''
Solution = Solution()
print(Solution.maxLengthBetweenEqualCharacters("aa"))
print(Solution.maxLengthBetweenEqualCharacters("abca")) 
print(Solution.maxLengthBetweenEqualCharacters("cbzxy"))
print(Solution.maxLengthBetweenEqualCharacters("cabbac"))