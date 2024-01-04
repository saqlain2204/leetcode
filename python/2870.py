'''
2870. Minimumnumber of operations to make Array Empty
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

'''
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        dict = {}
        ans = 0
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for j in dict:
            if dict[j] == 1:
                return -1
            ans += dict[j] // 3
            if dict[j] % 3 != 0:
                ans += 1
        return ans
        
'''
Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

Testcase:
Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4

Input: nums = [2,1,2,2,3,3]
Output: -1
'''
Solution = Solution()
print(Solution.minOperations([2,3,3,2,2,4,2,3,4]))
print(Solution.minOperations([2,1,2,2,3,3]))
