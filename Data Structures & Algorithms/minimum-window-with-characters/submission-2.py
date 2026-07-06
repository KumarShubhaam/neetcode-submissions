class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        for c in t:
            d1[c] = d1.get(c, 0) + 1

        # print(d1)
        indices = []
        for i, c in enumerate(s):
            if c in d1:
                indices.append(i)

        len_s = len(s)
        output = ""
        min_len = len_s + 1
        for i1, l in enumerate(indices):
            d2 = {}
            for i2 in range(i1, len(indices)):
                r = indices[i2]
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
