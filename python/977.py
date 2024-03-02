'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
'''
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums

'''
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Test Cases:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''
print(Solution().sortedSquares([-4,-1,0,3,10])) # [0,1,9,16,100]
print(Solution().sortedSquares([-7,-3,2,3,11])) # [4,9,9,49,121]
