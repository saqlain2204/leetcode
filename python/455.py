'''
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
'''


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        count, i, j = 0, 0, 0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count += 1
                i += 1
            j += 1
        return count
    

'''
Constraints:
1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1

Testcases:
[1,2,3], [1,1] -> 1
[1,2], [1,2,3] -> 2
[10,9,8,7], [5,6,7,8] -> 2
'''

Solution = Solution()
print(Solution.findContentChildren([1,2,3], [1,1]))
print(Solution.findContentChildren([1,2], [1,2,3]))
print(Solution.findContentChildren([10,9,8,7], [5,6,7,8]))
