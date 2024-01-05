'''
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
'''
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        import bisect
        length = 1
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
                length += 1
            else:
                index = bisect.bisect_left(temp, nums[i])
                temp[index] = nums[i]
        return length

'''
Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Testcase:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Input: nums = [0,1,0,3,2,3]
Output: 4
'''
Solution = Solution()
print(Solution.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution.lengthOfLIS([0,1,0,3,2,3]))