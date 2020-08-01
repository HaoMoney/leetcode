class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_s = ""
        max_len = 0
        for i in range(len(s)):
            tmp_index = final_s.find(s[i])
            if tmp_index >= 0:
                if tmp_index == len(final_s)-1:
                    final_s = s[i]
                else:
                    final_s = final_s[tmp_index+1:]
                    final_s += s[i]
            else:
                final_s += s[i]
            if len(final_s) > max_len:
                max_len = len(final_s)
        return max_len
