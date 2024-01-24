'''
561. Array Partition 
https://leetcode.com/problems/array-partition/
'''
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
    
'''
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104

Test case:
Input: nums = [1,4,3,2]
Output: 4

Input: nums = [6,2,6,5,1,2]
Output: 9

Input: nums = [1,2,3,2]
Output: 3
'''
print(Solution().arrayPairSum([1,4,3,2]))
print(Solution().arrayPairSum([6,2,6,5,1,2]))
print(Solution().arrayPairSum([1,2,3,2]))