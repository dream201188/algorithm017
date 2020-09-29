import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> resultMap = new HashMap<>();
        for (String str : strs) {
            char[] strArray = str.toCharArray();
            Arrays.sort(strArray);
            String newSortedStr = String.valueOf(strArray);
            if (!resultMap.containsKey(newSortedStr)) {
                resultMap.put(newSortedStr, new ArrayList<>());
            }
            resultMap.get(newSortedStr).add(str);
        }
        return new ArrayList(resultMap.values());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] strs = new String[] { "eat", "tea", "tan", "ate", "nat", "bat" };
        System.out.println(solution.groupAnagrams(strs));
    }
}
// @lc code=end
