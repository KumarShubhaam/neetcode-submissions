class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
            
        d1 = {}
        d2 = {}

        for i in range(n1):
            c1 = s1[i]
            c2 = s2[i]
            d1[c1] = d1.get(c1, 0) + 1
            d2[c2] = d2.get(c2, 0) + 1

        print(d1)
        print(d2)
        
        l = 0
        r = l + n1 - 1
        while l <= n2-n1:
            subStr = s2[l: r+1]
            print(subStr)
            print(d2)
            if d1 == d2:
                return True
            
            if d2[s2[l]] == 1:
                del d2[s2[l]]
            else:
                d2[s2[l]] -= 1
            l += 1

            r = r+1
            if r < n2:
                d2[s2[r]] = d2.get(s2[r], 0) + 1




            
        return False