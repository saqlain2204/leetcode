'''
2864. Maximum Odd Binary Number
https://leetcode.com/problems/maximum-odd-binary-number/
'''
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count('1')
        zeroes_count = s.count('0')
        ans = '1' * (ones_count-1) + '0' * zeroes_count + '1'
    
        return ans
        
'''
Constraints:
1 <= s.length <= 100
s consists only of '0' and '1'.
s contains at least one '1'.

Input: s = "010"
Output: "001"

Input: s = "0101"
Output: "1001"
'''
print(Solution().maximumOddBinaryNumber("010")) # "001"
print(Solution().maximumOddBinaryNumber("0101")) # "1001"
