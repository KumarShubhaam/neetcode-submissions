class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = { ')': '(', '}':'{', ']':'[' }
        stack = []

        for b in s:
            if b in closed_brackets and stack:
                # b is close bracket
                openBracket = stack.pop()
                if closed_brackets[b] != openBracket:
                    return False
            else:
                # b is open bracket
                stack.append(b)
                
        
        return True if not stack else False