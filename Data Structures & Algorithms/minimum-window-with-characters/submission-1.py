class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        for c in t:
            d1[c] = d1.get(c, 0) + 1

        # print(d1)
        len_s = len(s)
        output = ""
        min_len = len_s + 1
        for l in range(len_s):
            d2 = {}
            for r in range(l, len_s):
                c = s[r]
                subStr = s[l:r+1]
                # print(subStr)
                if c in d1:
                    if c not in d2:
                        d2[c] = 1
                    elif d2[c] < d1[c]:
                        d2[c] += 1

                    if d1 == d2 and len(subStr) <= min_len:
                        min_len = len(subStr)
                        # print('formed =', subStr)
                        output = subStr
                        break
        
        return output
