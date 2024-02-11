'''
1337. The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        temp_ans = []
        for i in range(0, len(mat)):
            count = 0
            for j in range(0, len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
            temp_ans.append(count)
        sorted_list = sorted(range(len(temp_ans)), key=lambda k: temp_ans[k])
        return sorted_list[:k]

'''
Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

Test Cases:
Input: mat = [[1,1,0,0,0],
                [1,1,1,1,0],
                [1,0,0,0,0],
                [1,1,0,0,0],
                [1,1,1,1,1]], k = 3

Output: [2,0,3]

Input: mat = [[1,0,0,0],
                [1,1,1,1],
                [1,0,0,0],
                [1,0,0,0]], k = 2
Output: [0,2]
'''
Solution = Solution()
print(Solution.kWeakestRows([[1,1,0,0,0],
                [1,1,1,1,0],
                [1,0,0,0,0],
                [1,1,0,0,0],
                [1,1,1,1,1]], 3))
print(Solution.kWeakestRows([[1,0,0,0],
                [1,1,1,1],
                [1,0,0,0],
                [1,0,0,0]], 2))