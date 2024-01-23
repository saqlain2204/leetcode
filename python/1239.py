'''
1239. Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
class Solution:
    def isUnique(self, string):
        return len(string) == len(set(string))

    def maxLength(self, arr: list[str]) -> int:
        max_len = 0
        combinations = [""]
        
        for i in range(len(arr)):
            new_combinations = []
            for combo in combinations:
                
                new_combo = combo + arr[i]

                if self.isUnique(new_combo):
                    max_len = max(max_len, len(new_combo))
                    new_combinations.append(new_combo)

            new_combinations.append(arr[i])
            combinations.extend(new_combinations)

        return max_len
    
'''
Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

Testcases:
Input: arr = ["un","iq","ue"]
Output: 4

Input: arr = ["cha","r","act","ers"]
Output: 6

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
'''
print(Solution().maxLength(["un","iq","ue"]))
print(Solution().maxLength(["cha","r","act","ers"]))
print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
