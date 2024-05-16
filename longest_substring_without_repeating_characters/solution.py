class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_s: str = ""
        longest_seq: int = 0

        idx: int = 0
        duplicated_char_idx: int = 0
        while idx != len(s):
            duplicated_char_idx = tmp_s.find(s[idx], duplicated_char_idx)
            duplicated_char_idx = (
                s.find(tmp_s[duplicated_char_idx], duplicated_char_idx)
                if duplicated_char_idx != -1
                else -1
            )

            if duplicated_char_idx != -1:
                # longest_seq = len(tmp_s) if len(tmp_s) > longest_seq else longest_seq
                tmp_s = ""
                idx = duplicated_char_idx + 1

            tmp_s += s[idx]
            idx += 1

            if idx == len(s):
                longest_seq = len(tmp_s) if len(tmp_s) > longest_seq else longest_seq

        return longest_seq
