import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub("[^0-9a-zA-Z]+", "", s)
        return s == s[::-1]
