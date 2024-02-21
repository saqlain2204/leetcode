'''
201. Bitwise AND of Numbers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right - 1)
        return right

'''
Constraints:
0 <= left <= right <= 2^31 - 1

Test cases:
Input: left = 5, right = 7
Output: 4

Input: left = 0, right = 0
Output: 0

Input: left = 1, right = 2147483647
Output: 0
'''
print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(1, 2147483647))