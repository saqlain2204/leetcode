/*
 * 111. Minimum Depth of Binary Tree
 * https://leetcode.com/problems/minimum-depth-of-binary-tree 
 */
public class q111 {}
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int minDepth(TreeNode root) 
    {
        if(root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        if(root.left==null && root.right == null) return 1;
        if(root.left==null) return right + 1;
        if(root.right== null) return left + 1;
        return Math.min(left, right) + 1;    
    }
    public static void main(String[] args) {
        Solution Solution = new Solution();
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        int result = Solution.minDepth(root);
        System.out.println("Result: " + result);
    }
}



/*
 * Constraints:
 * The number of nodes in the tree is in the range [0, 105].
 * -1000 <= Node.val <= 1000
 * Testcase:
 * [3,9,20,null,null,15,7]
 * [2,null,3,null,4,null,5,null,6]
 */
