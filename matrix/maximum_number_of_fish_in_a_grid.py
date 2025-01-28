# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid

"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    A land cell if grid[r][c] = 0, or
    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    Catch all the fish at cell (r, c), or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
"""

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_sum = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        # right, left, down, up
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] and not visited[row][col]:
                    current_sum = 0
                    
                    q = deque()
                    q.append((row, col))
                    
                    visited[row][col] = True

                    while q:
                        x, y = q.popleft()
                        current_sum += grid[x][y]

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            # valid coordinate
                            if 0 <= nx < m and 0 <= ny < n:
                                # must be water cell and not have been visited
                                if not visited[nx][ny] and grid[nx][ny]:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
                    
                    max_sum = max(max_sum, current_sum)
        
        return max_sum
