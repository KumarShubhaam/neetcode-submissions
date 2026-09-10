class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def index_in_grid(r: int, c: int) -> bool:
            if (r >= 0 and r < ROWS) and (c >= 0 and c < COLS):
                return True
            return False

        def countIslandAreaAndMark(r, c):
            grid[r][c] = 0
            count = 0
            for (dr,dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if index_in_grid(nr, nc) and grid[nr][nc] == 1:
                    # print(f"-> nr:{nr}, nc:{nc}")
                    count += countIslandAreaAndMark(nr, nc)
            return count + 1
        
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    result = max(result, countIslandAreaAndMark(r, c))

        return result