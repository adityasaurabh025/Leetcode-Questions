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
class Solution {
    Set<Integer> hs= new HashSet<>();
   public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set = new HashSet<>();
        return dfs(root, set, k);
    }

    public static boolean dfs(TreeNode root, Set<Integer> set, int target) {
        if (root == null) {
            return false;
        }

        if (set.contains(target - root.val)) {
            return true;
        }

        set.add(root.val);
        return dfs(root.left, set, target) || dfs(root.right, set, target);
    }
}




// Using List
/* class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> numsList = new ArrayList<>();
        inOrder(numsList, root);

        int len = numsList.size();
        for (int i = 0, j = len - 1; i < j; ) {
            int sum = numsList.get(i) + numsList.get(j);
            if (sum < k) {
                i++;
            } else if (sum > k) {
                j--;
            } else {
                return true;
            }
        }

        return false;
    }

    private void inOrder(List<Integer> nums, TreeNode root) {
        if (root == null) {
            return;
        }

        inOrder(nums, root.left);
        nums.add(root.val);
        inOrder(nums, root.right);
    }
}


 Since the tree is binary search tree, so we can traversal this tree inOrder, and the list will arranged in ascending order. You can refer to Tree Traversals: PreOrder, InOrder and PostOrder | Traverse Algorithms All In One .

 Then we can use two pointers to point to the head and tail.

 Time complexity: O(N), Space complexity: O(N)
 */