'''
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
'''
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        unique = set()
        repeated = 0
        e_sum = n*(n+1)//2
        a_sum = 0
        for i in nums:
            if i in unique:
                repeated = i
            unique.add(i)
            a_sum += i
        
        missing = e_sum - a_sum + repeated
        return [repeated, missing]

'''
Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4

Testcases:
Input: nums = [1,2,2,4]
Output: [2,3]

Input: nums = [1,1]
Output: [1,2]

Input: nums = [2,2]
Output: [2,1]
'''
print(Solution().findErrorNums([1,2,2,4]))
print(Solution().findErrorNums([1,1]))
print(Solution().findErrorNums([2,2]))