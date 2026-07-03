class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[a-zA-Z0-9]"
        
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            while l < n-1 and not re.match(regex, s[l]):
                l += 1
            while r > 0 and not re.match(regex, s[r]):
                r -= 1
            # print(s[l], '==', s[r])
            if s[l].lower() != s[r].lower() and re.match(regex, s[l]) and re.match(regex, s[r]):
                return False
            l += 1
            r -= 1

        return True 