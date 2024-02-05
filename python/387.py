'''
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for i in range(0, len(s)):
            if s[i] not in ans:
                ans[s[i]] = 1
            else:
                ans[s[i]] += 1
        for i in range(0, len(s)):
            if ans[s[i]] == 1:
                return i
        return -1
        
'''
Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.

Test Cases:
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
'''
Solution = Solution()
print(Solution.firstUniqChar("leetcode"))
print(Solution.firstUniqChar("loveleetcode"))
print(Solution.firstUniqChar("aabb"))