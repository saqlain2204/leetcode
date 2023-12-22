'''
    1422. Maximum Score After Splitting a String
    https://leetcode.com/problems/maximum-score-after-splitting-a-string/
'''

class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            left_sum = left.count('0')
            right_sum = right.count('1')

            maxi = max(maxi, left_sum + right_sum)

        return maxi
    
'''
    Constraints:
        2 <= s.length <= 500
        The string s consists of characters '0' and '1' only.
    
    Test Casse 1:
        Input: s = "011101"
        Output: 5 
    Test Case 2:
        Input: s = "00111"
        Output: 5
'''

Solution = Solution()
print(Solution.maxScore("011101"))
print(Solution.maxScore("00111"))
