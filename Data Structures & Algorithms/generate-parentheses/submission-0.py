class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opened, closed, curr):
            if opened >= n and closed >= n:
                res.append("".join(curr))
                return
            
            if opened < n:
                opened += 1
                curr.append('(')
                dfs(opened, closed, curr)
                opened -= 1
                curr.pop()
            if closed < n and closed < opened:
                closed += 1
                curr.append(')')
                dfs(opened, closed, curr)
                closed -= 1
                curr.pop() 
            return
            
        dfs(0, 0, [])
        return res
        