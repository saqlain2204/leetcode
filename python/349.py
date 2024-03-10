'''
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
'''
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        lst = []
        for i in nums1:
            if i in nums2:
                lst.append(i)
        lst = list(set(lst))
        return lst

'''
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Test cases:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''
print(Solution().intersection([1,2,2,1], [2,2])) # [2]
print(Solution().intersection([4,9,5], [9,4,9,8,4])) # [9,4]