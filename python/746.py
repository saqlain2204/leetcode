'''
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
'''
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[n-1], cost[n-2])

'''
Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999

Example 1:
Input: cost = [10, 15, 20]
Output: 15

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
'''
print(Solution().minCostClimbingStairs([10, 15, 20])) # 15
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6