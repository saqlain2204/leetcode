'''
2149. Rearrange Array Elements By Sign
https://leetcode.com/problems/rearrange-array-elements-by-sign/
'''
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans_pos = []
        ans_neg = []
        ans = []
        for num in nums:
            if num < 0:
               ans_neg.append(num)
            else:
                ans_pos.append(num)

        for i in range(0, len(ans_pos)):
            ans.append(ans_pos[i])
            ans.append(ans_neg[i])
        
        return ans
    
'''
Constraints:
2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.

Test Cases:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Input: nums = [-1,1]
Output: [1,-1]
'''
Solution = Solution()
print(Solution.rearrangeArray([3,1,-2,-5,2,-4]))
print(Solution.rearrangeArray([-1,1]))