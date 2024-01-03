'''
2125. Number of leaser beams in a bank
https://leetcode.com/problems/number-of-leaser-beams-in-a-bank/
'''
'''
0 -> the cell is empty
1 -> the cell has a security device

there is a laser beam b/w 2 security devices if the conditions are met


'''


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        temp = 0
        for i in bank:
            count = i.count('1')
            if count == 0:
                continue
            else:
                ans += temp * count
                temp = count
        return ans
             
'''
Constraints:
m == bank.length
n == bank[i].length
1 <= m, n <= 100
bank[i][j] is either '0' or '1'.

Testcase:
Input: bank = ["011001","000000","010100","001000"]
Output: 8

Input: bank = ["000","111","000"]
Output: 0

'''
Solution = Solution()
print(Solution.numberOfBeams(["011001","000000","010100","001000"]))
print(Solution.numberOfBeams(["000","111","000"]))
