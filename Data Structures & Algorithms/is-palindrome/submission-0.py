import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[a-zA-Z0-9]"
        a = re.findall(regex, s)
        string = ("".join(a)).lower()
        return True if string == string[::-1] else False