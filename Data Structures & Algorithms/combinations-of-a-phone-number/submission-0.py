class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return

            d = digits[i]
            for char in dial[d]:
                curr += char
                dfs(i+1, curr)
                curr = curr[:-1]
            
            return
        dfs(0, "")
        return res if digits else []

            