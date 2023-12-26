public class q108 {}
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
    public TreeNode sortedArrayToBST(int[] nums) {
        return create(nums, 0, nums.length - 1);
    }
    public TreeNode create(int nums[], int l, int r)
    {
        if(l>r)
            return null;
        
        int mid = l + (r - l)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = create(nums, l, mid - 1);
        root.right = create(nums, mid + 1, r);

        return root;
    }
    public static void main(String[] args) {
        Solution Solution = new Solution();
        int[] nums = {-10,-3,0,5,9};
        TreeNode result = Solution.sortedArrayToBST(nums);
        System.out.println("Result: " + result);
        int[] nums2 = {1,3};
        TreeNode result2 = Solution.sortedArrayToBST(nums2);
        System.out.println("Result: " + result2);
    }
}

// Constraints:
// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums is sorted in a strictly increasing order.
// Testcase:
// [-10,-3,0,5,9] -> [0,-3,9,-10,null,5]
// [1,3] -> [3,1]



