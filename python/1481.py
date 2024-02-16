'''
1481. Least Number of Unique Integers after K Removals
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
'''
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        ans = {}
        for num in arr:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1

        elements = sorted(ans.items(), key = lambda x:x[1])

        for key, val in elements:
            if val <= k:
                k -= val
                del ans[key]
            else:
                break
        return len(ans)

'''
Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

Test Cases:
Input: arr = [5,5,4], k = 1
Output: 1

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
'''
Solution = Solution()
print(Solution.findLeastNumOfUniqueInts([5,5,4], 1))
print(Solution.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
        