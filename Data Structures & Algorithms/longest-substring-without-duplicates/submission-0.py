class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        length = 0
        seen = set()
        l = 0
        r = 0
        while r < n:
            char = s[r]
            # print(char, s[l:r+1])
            if char not in seen:
                length = max(length, (r - l + 1))
                seen.add(char)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        
        return length