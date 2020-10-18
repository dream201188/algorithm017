import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int length = nums.length;
        List<List<Integer>> res = new ArrayList<>();
        if (length == 0)
            return res;
        boolean[] used = new boolean[length];
        List<Integer> path = new LinkedList<>();
        dfs(0, length, nums, used, path, res);
        return res;
    }

    private void dfs(int index, int length, int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> res) {
        if (index == length) {
            res.add(new LinkedList<>(path));
            return;
        }
        for (int i = 0; i < length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.add(nums[i]);
                dfs(index + 1, length, nums, used, path, res);
                used[i] = false;
                path.remove(index);
            }
        }
    }
}
// @lc code=end
