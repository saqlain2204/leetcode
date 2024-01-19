'''
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
'''
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(1, rows):
            for j in range(cols):
                matrix[i][j] += min(
                    matrix[i-1][max(j-1, 0)],
                    matrix[i-1][j],
                    matrix[i-1][min(j+1, cols-1)]
                )

        return min(matrix[-1])
                

'''
Constraints:
1 <= rows, cols <= 100
-100 <= matrix[i][j] <= 100

Test case:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

Input: matrix = [[-19,57],[-40,-5]]
Output: -59

Input: matrix = [[-48]]
Output: -48
'''
print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(Solution().minFallingPathSum([[-19,57],[-40,-5]]))
print(Solution().minFallingPathSum([[-48]]))