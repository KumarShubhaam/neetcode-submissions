class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1 = sorted(s1)

        for l in range(n2-n1+1):
            w = sorted(s2[l: l+n1])
            # print(w)
            if w == s1:
                return True


        return False
