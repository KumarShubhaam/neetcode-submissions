class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def traverse(r, c, path, visited):
            if r >= len(board) or c >= len(board[0]):
                return False

            directions = [(0,1), (0,-1), (1,0), (-1,0)]  #(r,c)

            path += board[r][c]
            if path == word:
                return True
            if path[-1] != word[len(path)-1]:
                return False           
            
            visited.add((r,c))

            for (x,y) in directions:
                newR = r+x
                newC = c+y
                if (newR, newC) not in visited and (newR >= 0 and newC >= 0):
                    ans = traverse(newR, newC, path, visited)
                    if ans:
                        return True

            visited.remove((r,c))
            path = path[:-1]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    ans = traverse(i, j, "", set())
                    if ans:
                        return ans

        return False

                

            

                    
                

