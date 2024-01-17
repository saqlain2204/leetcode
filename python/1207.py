'''
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
'''
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict = {}
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        unique = set()
        for i in dict.items():
            if i[1] in unique:
                return False
            else:
                unique.add(i[1])

        return True

        
'''
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Test case:
Input: arr = [1,2,2,1,1,3]
Output: true

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))