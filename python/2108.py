'''
2108. Find First Palindromic String in the array
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
'''
class Solution:
    def isPalindrome(self, word: str) -> bool:
        start = 0
        end = len(word) - 1
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
    
'''
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.

Test Cases:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"

Input: words = ["notapalindrome","racecar"]
Output: "racecar"

Input: words = ["def","ghi"]
Output: ""
'''
Solution = Solution()
print(Solution.firstPalindrome(["abc","car","ada","racecar","cool"]))
print(Solution.firstPalindrome(["notapalindrome","racecar"]))
print(Solution.firstPalindrome(["def","ghi"]))


    
        