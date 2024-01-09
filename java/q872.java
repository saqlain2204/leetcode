// 872. Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/


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
import java.util.*;
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();

        check(list1, root1);
        check(list2, root2);
        if(list1.equals(list2)) return true;
        return false;
    }
    public void check(ArrayList<Integer>list, TreeNode root)
    {
        if(root == null) return;

        if(root.left == null && root.right == null)
        {
            list.add(root.val);
            return;
        }

        check(list, root.left);
        check(list, root.right);
    }
}
