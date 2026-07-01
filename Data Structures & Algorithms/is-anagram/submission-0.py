class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        character = {}
        
        for c in s:
            character[c] = character.get(c, 0) + 1
        
        for c in t:
            character[c] = character.get(c, 0) - 1

        for v in character.values():
            if v > 0:
                return False
        return True

