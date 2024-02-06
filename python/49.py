'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in ans:
                ans[sorted_word] = []
            ans[sorted_word].append(word)
        return list(ans.values())

'''
Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Test Cases:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''
Solution = Solution()
print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams([""]))
print(Solution.groupAnagrams(["a"]))
