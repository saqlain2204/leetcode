// 455. Assign Cookies
// https://leetcode.com/problems/assign-cookies/

import java.util.Arrays;

public class q455 {}
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int result = 0;
        int i = 0;
        int j = 0;
        while(i<g.length && j<s.length)
        {
            if(s[j]>=g[i])
            {
                result++;
                i++;
                j++;
            }
            j++;
        }
        return result;
    }
    public static void main(String[] args) {
        Solution Solution = new Solution();
        int[] g = {1,2,3};
        int[] s = {1,1};
        int result = Solution.findContentChildren(g, s);
        System.out.println("Result: " + result);
        int[] g2 = {1,2};
        int[] s2 = {1,2,3};
        int result2 = Solution.findContentChildren(g2, s2);
        System.out.println("Result: " + result2);
    }
}

// Constraints:
// 1 <= g.length <= 3 * 104
// 0 <= s.length <= 3 * 104
// 1 <= g[i], s[j] <= 231 - 1
// Testcase:
// g = [1,2,3], s = [1,1] -> 1
// g = [1,2], s = [1,2,3] -> 2


