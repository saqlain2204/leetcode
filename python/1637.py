'''

    1637. Widest Vertical area between 2 points containing no points.

    https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

'''

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:

        '''
            Args: points = a 2D list of integers
            Returns: max_width = the maximum width of vertical area between two points containing no points
        '''
        
        points.sort(key = lambda x:x[0])

        max_width = 0
        for i in range(1, len(points)):
            width = points[i][0]-points[i-1][0]
            max_width = max(width, max_width)

        return max_width

    
''' 
    Test Cases & Constraints:

        Constraints: 1 <= points.length <= 10^5
                                points[i].length == 2
                                0 <= points[i][0], points[i][1] <= 10^9

        Case 1: points = [[8,7],[9,9],[7,4],[9,7]]
            Answer: 1
        Case 2: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
            Answer: 3
'''
    
Solution = Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
print(Solution.maxWidthOfVerticalArea(points))
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(Solution.maxWidthOfVerticalArea(points))