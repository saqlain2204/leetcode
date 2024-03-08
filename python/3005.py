'''
3005. Count Elements with Maximum Frequency
https://leetcode.com/problems/count-elements-with-maximum-frequency/
'''
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        ans = [0]*(max(nums) + 1)
        for i in range(0, len(nums)):
            ans[nums[i]] += 1
        count = max(ans)
        final_ans = 0
        for i in ans:
            if count == i:
                final_ans += i
        return final_ans
        
'''
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Test cases:
Input: nums = [1,2,2,3,1,4]
Output: 4

Input: nums = [1,2,3,4,5]
Output: 5
'''
print(Solution().maxFrequencyElements([1,2,2,3,1,4])) # 4
print(Solution().maxFrequencyElements([1,2,3,4,5])) # 5