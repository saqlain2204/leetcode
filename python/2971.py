'''
2971. Find Polygon with the Largest Perimeter
https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
'''
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        if len(nums) < 3: return -1
        nums.sort()
        sum_values = 0
        ans =  -1
        for num in nums:
            if num < sum_values:
                ans = num + sum_values
            sum_values += num
        return ans

'''
Constraints:
3 <= n <= 105
1 <= nums[i] <= 109

Test Cases:
Input: nums = [5,5,5]
Output: 15

Input: nums = [1,12,1,2,5,50,3]
Output: 12

Input: nums = [5,5,50]
Output: -1
'''
Solution = Solution()
print(Solution.largestPerimeter([5,5,5]))
print(Solution.largestPerimeter([1,12,1,2,5,50,3]))
print(Solution.largestPerimeter([5,5,50]))
