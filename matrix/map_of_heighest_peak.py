from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        m, n = len(isWater), len(isWater[0])
        
        cellHeights = [[-1 for _ in range(n)] for _ in range(m)]
        cellQueue = deque()

        for row in range(m):
            for col in range(n):
                if isWater[row][col]:
                    cellQueue.append((row, col))
                    cellHeights[row][col] = 0
        
        nextHeight = 1
        
        while cellQueue:
            layerSize = len(cellQueue)
            
            for cell in range(layerSize):
                row, col = cellQueue.popleft()

                for d in range(4):
                    neighborX = row + dx[d]
                    neighborY = col + dy[d]

                    # neighbor coordinates must be valid
                    if not (0 <= neighborX < m and 0 <= neighborY < n):
                        continue

                    # not visited
                    if cellHeights[neighborX][neighborY] == -1:
                        cellHeights[neighborX][neighborY] = nextHeight
                        cellQueue.append((neighborX, neighborY))
                
            nextHeight += 1

        return cellHeights
        