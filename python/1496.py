'''
1496. Path Crossing
https://leetcode.com/problems/path-crossing/

'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        '''
        Args: 
            path: string of characters in {'N', 'S', 'E', 'W}
        Returns:
            True if path crosses itself, False otherwise
        '''
        visited = []
        x = 0
        y = 0
        visited.append([x,y])
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == 'S':
                y -= 1
            else:
                x -= 1
            if [x,y] in visited:
                return True
            visited.append([x,y])
        return False 

        
'''
    Constraints:
        1 <= path.length <= 10^4
        path will only consist of characters in {'N', 'S', 'E', 'W}

    Test Case 1:
        Input: path = "NES"
        Output: false 

    Test Case 2:
        Input: path = "NESWW"
        Output: true
    
'''

Solution = Solution()
print(Solution.isPathCrossing("NES"))
print(Solution.isPathCrossing("NESWW"))
