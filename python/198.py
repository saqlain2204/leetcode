'''
198. House Robber
https://leetcode.com/problems/house-robber/

Solution referred to: https://leetcode.com/problems/house-robber/solutions/4600148/beats-100-c-java-python-js-explained-with-video-dynamic-programming-space-optimized/
'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        rob, norob = 0, 0
        for num in nums:
            newRob = norob + num
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
        return max(rob, norob)
    
'''
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

Testcases:
Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12

Input: nums = [2,1,1,2]
Output: 4
'''
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))