/*
 * @lc app=leetcode.cn id=242 lang=java
 *
 * [242] 有效的字母异位词
 * 一个表，index 是阿斯科码 值是出现次数 第一个字符串遍历后积累次数，第二个字符串减去次数，如果小于0，
 * 说明两个字符串里面的字母不一致，s里面没有，t里面有
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] tables = new int[26];
        for (int i = 0; i < s.length(); i++) {
            tables[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            int temp = --tables[t.charAt(i) - 'a'];
            if (temp < 0) {
                return false;
            }
        }
        return true;
    }

}
// @lc code=end
