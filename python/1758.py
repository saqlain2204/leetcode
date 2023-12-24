'''
1758: Minimum Changes To Make Alternating Binary String
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

'''

class Solution:
    def minOperations(self, s: str) -> int:
        count_same = self.count(s, s[0])
        count_changed = self.count(s, '1' if s[0] == '0' else '0')
        return min(count_same, count_changed+1)


    def count(self, s: str, first: str) -> int:
        stack = []
        stack.append(first)  
        count = 0
        for i in range(1, len(s)):
            if stack[-1] == s[i]:
                count += 1
                if stack[-1] == '0':
                    stack.append('1')
                else:
                    stack.append('0')
            else:
                stack.append(s[i])
        return count
    
'''

Constraints:
    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.

Test Case 1:
    Input: s = "0100"
    Output: 1

Test Case 2:
    Input: s = "10"
    Output: 0
'''

Solution = Solution()
print(Solution.minOperations("0100"))
print(Solution.minOperations("10"))
