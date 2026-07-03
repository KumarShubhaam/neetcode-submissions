class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[a-zA-Z0-9]"
        string = []
        for c in s:
            if re.match(regex, c):
                string.append(c.lower())
        # print(string)
        n = len(string)
        l = 0
        r = n-1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1

        return True 