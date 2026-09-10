class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def index_in_grid(r: int, c: int) -> bool:
            if (r >= 0 and r < ROWS) and (c >= 0 and c < COLS):
                return True
            return False

        def markWater(r, c):
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for (dr,dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if index_in_grid(nr, nc) and grid[nr][nc] == "1":
                    # print(f"-> nr:{nr}, nc:{nc}")
                    markWater(nr, nc)
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # print(f"for r:{r}, c:{c}")
                    count += 1
                    markWater(r, c)

        return count
