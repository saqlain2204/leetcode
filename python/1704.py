'''
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
'''
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        count_a, count_b = 0, 0
        for letter in a:
            if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
                count_a += 1
        
        for letter in b:
            if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
                count_b += 1

        return count_a == count_b
    
'''
Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

Test Cases:
"book" -> true
"textbook" -> false
'''

print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))