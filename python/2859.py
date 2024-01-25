'''
2859. Sum of Values at indices with K set bits
https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits
'''

class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        return sum(x for i, x in enumerate(nums) if bin(i).count('1') == k)
    
'''
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 105
0 <= k <= 10

Test case:
Input: nums = [5,10,1,5,2], k = 1
Output: 13

Input: nums = [4,3,2,1], k = 2
Output: 1
'''
print(Solution().sumIndicesWithKSetBits([5,10,1,5,2], 1))
print(Solution().sumIndicesWithKSetBits([4,3,2,1], 2))