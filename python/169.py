'''
169. Majority Element
https://leetcode.com/problems/majority-element/
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)//2
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1
            if ans[num] > n:
                return num
        return -1

'''
Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Test Cases:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
Solution = Solution()
print(Solution.majorityElement([3,2,3]))
print(Solution.majorityElement([2,2,1,1,1,2,2]))