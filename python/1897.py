'''
1897. Redistribute Characters to Make All Strings Equal
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

'''
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        ans = {}
        for i in words:
            for j in i:
                if j not in ans:
                    ans[j] = 1
                else:
                    ans[j] += 1
        for keys in ans:
            if ans.get(keys) % len(words) != 0:
                return False

        return True        
    
'''
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Testcases:
["abc","aabc","bc"] -> true
["ab","a"] -> false
["a","b"] -> false
["abc","cba"] -> true
["ab","ab"] -> true

'''
print(Solution().makeEqual(["abc","aabc","bc"]))
print(Solution().makeEqual(["ab","a"]))
print(Solution().makeEqual(["a","b"]))
print(Solution().makeEqual(["abc","cba"]))
print(Solution().makeEqual(["ab","ab"]))