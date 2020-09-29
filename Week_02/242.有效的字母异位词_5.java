
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
        int[] tables = new int[26];
        for (String str : strs) {
            Arrays.fill(tables, 0);
            char[] strArray = str.toCharArray();
            StringBuilder sb = new StringBuilder();

            for (char tmp : strArray) {
                tables[tmp - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                sb.append("#");
                sb.append(tables[i]);
            }
            String key = sb.toString();
            if (!resultMap.containsKey(key))
                resultMap.put(key, new ArrayList<>());
            resultMap.get(key).add(str);
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
