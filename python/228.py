'''
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/
'''

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums == []:
            return []

        ans = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == ans[-1][-1] + 1:
                ans[-1][-1] = nums[i]
            else:
                ans.append([nums[i], nums[i]])

        ans_string = []
        for i in ans:
            if i[0] == i[1]:
                ans_string.append(str(i[0]))
            else:
                ans_string.append(str(i[0]) + '->' + str(i[1]))

        return ans_string

'''
Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums contains sorted, unique numbers sorted in ascending order.

Testcases:
[0,1,2,4,5,7] -> ["0->2","4->5","7"]
[0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]
[] -> []
[-1] -> ["-1"]
[0] -> ["0"]
'''
print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([]))
print(Solution().summaryRanges([-1]))
print(Solution().summaryRanges([0]))