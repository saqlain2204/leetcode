/*
  1637. Widest Vertical Area Between Two Points Containing No Points
  https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
*/

import java.util.*;
class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int max = 0;
        Arrays.sort(points, (a, b) -> a[0] - b[0]);
        for(int i = 1; i < points.length; i++) {
            max = Math.max(max, points[i][0] - points[i - 1][0]);
        }
        return max;
    }
}

/*
 * Test Case & Constraints
 * Constraints:
 * 2 <= points.length <= 10^5
 * points[i].length == 2
 * 0 <= points[i][0], points[i][1] <= 10^9
 * 
 * Test Case:
 *  Case 1: [[8,7],[9,9],[7,4],[9,7]]
 *  Ans: 1
 * 
 * Case 2: [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
 * Ans: 3
 */

public class q1637 {
    public static void main(String[] args) {
        int[][] points = {{3,1},{9,0},{1,0},{1,4},{5,3},{8,8}};
        Solution sol = new Solution();
        System.out.println(sol.maxWidthOfVerticalArea(points));
        int[][] points2 = {{8,7},{9,9},{7,4},{9,7}};
        System.out.println(sol.maxWidthOfVerticalArea(points2));
    }
}
