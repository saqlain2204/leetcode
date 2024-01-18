'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
'''
cache = {0:0, 1:1}
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n in cache:
                return cache[n]
            result = fib(n-1) + fib(n-2)
            cache[n] = result
            return result
        return fib(n+1)
    
'''
Constraints:
1 <= n <= 45

Test case:
Input: n = 2
Output: 2

Input: n = 3
Output: 3

Input: n = 4
Output: 5
'''

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))