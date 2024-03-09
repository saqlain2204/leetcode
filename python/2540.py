'''
2540. Minimum Common Value
https://leetcode.com/problems/minimum-common-value/
'''
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        return -1

'''
Constraints:
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.

Test cases:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
'''
print(Solution().getCommon([1,2,3], [2,4])) # 2
print(Solution().getCommon([1,2,3,6], [2,3,4,5])) # 2