'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum1 = sum(nums)
        required_sum = sum(range(1, len(nums)+1))
        return required_sum - sum1
    
'''
Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

Test cases:
Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
'''
print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))