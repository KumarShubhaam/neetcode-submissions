class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        d1 = {}
        for c in s1:
            d1[c] = d1.get(c, 0) + 1
        print(d1)

        l = 0
        r = n1
        while r <= n2:
            subStr = s2[l: r]
            print(subStr)
            d2 = {}
            for c in subStr:
                d2[c] = d2.get(c, 0) + 1
            print(d2)
            if d1 == d2:
                return True
            l += 1
            r += 1

        return False