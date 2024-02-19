'''
231. Power of Two
https://leetcode.com/problems/power-of-two/
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(-31, 32):
            if n == 2**i:
                return True
        return False

'''
Constraints:
-2^31 <= n <= 2^31 - 1

Test cases:
Input: n = 1
Output: true

Input: n = 16
Output: true

Input: n = 3
Output: false
'''
print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))