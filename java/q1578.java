// 1578. Minimum Deletion Cost to Avoid Repeating Letters
// https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

public class q1578 {}
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int prev = 0;
        int ans = 0;
        for(int i=1;i<neededTime.length;i++)
        {
            if(colors.charAt(prev) != colors.charAt(i))
                prev = i;
            else
            {
                if(neededTime[prev] < neededTime[i])
                {
                    ans += neededTime[prev];
                    prev = i;
                }
                else
                    ans += neededTime[i];
                
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        Solution Solution = new Solution();
        String colors = "abaac";
        int[] neededTime = {1,2,3,4,5};
        int result = Solution.minCost(colors, neededTime);
        System.out.println("Result: " + result);
        String colors2 = "abc";
        int[] neededTime2 = {1,2,3,4};
        int result2 = Solution.minCost(colors2, neededTime2);
        System.out.println("Result: " + result2);
    }
}

// Constraints:
// n == neededTime.length
// 1 <= n <= 105
// 1 <= neededTime[i] <= 109
// colors.length == n
// colors[i] is either 'a', 'b', or 'c'.
// Testcase:
// "abaac"
// [1,2,3,4,5]
// "abc"
// [1,2,3,4]
