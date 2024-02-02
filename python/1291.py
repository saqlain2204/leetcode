'''
1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        corpus = "123456789"
        ans = []
        for i in range(0, len(corpus)):
            for j in range(i+1, len(corpus)+1):
                temp = int(corpus[i:j])
                if low <= temp <= high:
                    ans.append(temp)
        ans.sort()
        return ans

'''
Constraints:
10 <= low <= high <= 10^9

Test Cases:
Input: low = 100, high = 300
Output: [123,234]

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

'''

Solution = Solution()
print(Solution.sequentialDigits(100, 300))
print(Solution.sequentialDigits(1000, 13000))
    