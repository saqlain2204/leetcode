'''
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos, ans = 0, 0
        for i in reversed(columnTitle):
            sum1 = ord(i) - 64
            ans += sum1 * 26**pos
            pos += 1
        return ans
    
'''
Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

Test Cases:
Input: columnTitle = "A"
Output: 1

Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701
'''
print(Solution().titleToNumber("A"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("ZY"))
print(Solution().titleToNumber("FXSHRXW"))