// 938. Range Sum of BST
// https://leetcode.com/problems/range-sum-of-bst/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 /*
 if low is greater then the root, then check for the right side
 else
 check for the left side and then add

  */
  class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {

        int sum = 0;
        if(root == null) return 0;
        if(root.val >= low && root.val <= high)
        {
            sum += root.val;
        } 
        if(root.val > low)
        {
            sum += rangeSumBST(root.left, low, high);
        }
        if(root.val < high)
        {
            sum += rangeSumBST(root.right, low, high);
        }
        return sum;
    }
}

// Constraints:
// The number of nodes in the tree is in the range [1, 2 * 104].
// 1 <= Node.val <= 105 
// 1 <= low <= high <= 105  
// All Node.val are unique.

// TestCases:
// [10,5,15,3,7,null,18] -> 32
// [10,5,15,3,7,13,18,1,null,6] -> 23

