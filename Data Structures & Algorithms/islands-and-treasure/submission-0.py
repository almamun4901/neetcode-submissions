class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        q = deque()
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                
                if grid[r][c] != INF:
                    continue
                
                
                grid[r][c] = 1 + grid[row][col]
                q.append((r,c))

                
