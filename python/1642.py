'''
1642. Furthest Building You can Reach
https://leetcode.com/problems/furthest-building-you-can-reach/
'''
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for height in range(len(heights) -1):
            diff = heights[height+1] - heights[height]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return height
        return len(heights) - 1
    
'''
Constraints:
1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length

Test Cases:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
'''