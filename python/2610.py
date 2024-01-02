'''
2610. Convert an Array into 2D
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
'''
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for num in nums:
            if not result:
                result.append([num])
            else:
                added = False
                for row in result:
                    if num > row[-1]:
                        row.append(num)
                        added = True
                        break
                if not added:
                    result.append([num])

        return result
    

'''
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= nums.length

Test Cases:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
'''

print(Solution().findMatrix([1,3,4,1,2,3,1]))
print(Solution().findMatrix([1,2,3,4]))