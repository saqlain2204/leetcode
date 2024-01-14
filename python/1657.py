'''
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        for letter1 in word1:
            if letter1 not in word2:
                return False
        if len(word1) != len(word2):
            return False
        dict1 = {}
        dict2 = {}
        for i in word1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for j in word2: 
            if j not in dict2:
                dict2[j] = 1
            else:
                dict2[j] += 1

        sortedDict1 = dict(sorted(dict1.items(), reverse=True, key=lambda item: item[1]))
        sortedDict2 = dict(sorted(dict2.items(), reverse=True, key=lambda item: item[1]))

        for i, j in zip(sortedDict1.items(), sortedDict2.items()):
            if i[1] != j[1]:
                return False
        return True
    
'''
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

Test case:
"abc", "bca" -> true
"a", "aa" -> false
"cabbba", "abbccc" -> true
"cabbba", "aabbss" -> false
'''

print(Solution().closeStrings("abc", "bca"))
print(Solution().closeStrings("a", "aa"))
print(Solution().closeStrings("cabbba", "abbccc"))
print(Solution().closeStrings("cabbba", "aabbss"))