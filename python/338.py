'''
338. Counting Bits
https://leetcode.com/problems/counting-bits/
'''
class Solution:
    def countBits(self, n: int) -> list[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
    
'''
Constraints:
0 <= n <= 10^5

Test Cases:
Input: n = 2
Output: [0,1,1]

Input: n = 5
Output: [0,1,1,2,1,2]
'''
Solution = Solution()
print(Solution.countBits(2))
print(Solution.countBits(5))
