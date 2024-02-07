'''
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = {}
        for letter in s:
            if letter not in ans:
                ans[letter] = []
            ans[letter].append(letter)

        check = dict(sorted(ans.items(), key=lambda item: len(item[1]), reverse=True))
        lists = list(check.values())
        temp = ''
        for lister in lists:
            temp += ''.join(lister)
        return temp

        

'''
Constraints:
1 <= s.length <= 5 * 10^5
s consists of printable ASCII characters.

Test Cases:
Input: s = "tree"
Output: "eert"

Input: s = "cccaaa"
Output: "aaaccc"

Input: s = "Aabb"
Output: "bbAa"
'''
Solution = Solution()
print(Solution.frequencySort("tree"))
print(Solution.frequencySort("cccaaa"))
print(Solution.frequencySort("Aabb"))
