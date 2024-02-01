'''
2966. Divide Array Into Arrays With Max Difference
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
'''
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        size = len(nums)
        nums.sort()
        req_size = len(nums)//3
        ans = []
        temp = []
        for i in range(0, size):
            if len(temp) == 0:
                temp.append(nums[i])
            else:
                if nums[i] - temp[-1] <= k and nums[i] - temp[0] <= k:
                    temp.append(nums[i])
            if len(temp) ==  3:
                ans.append(temp)
                temp = []
        if len(ans) == req_size:
            return ans
        return []

'''
Constraints:
n == nums.length
1 <= n <= 105
n is a multiple of 3.
1 <= nums[i] <= 105
1 <= k <= 105

Test Cases:
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]

Input: nums = [1,3,3,2,7,3], k = 3
Output: []
'''

Solution = Solution()
print(Solution.divideArray([1,3,4,8,7,9,3,5,1], 2))
print(Solution.divideArray([1,3,3,2,7,3], 3))