from typing import List
###################### 미완성
grid = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]

def printAddress(grid) -> List[List[int]]:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    globalStack = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 1:
                continue

            stack = [(row,col)]

            while stack:
                x,y = stack.pop()
                globalStack = grid[x][y]

                grid[x][y] = 9
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = grid[nx][ny]




    return grid

result = printAddress(grid)
print(result)