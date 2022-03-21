grid = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,1],
    [0,0,1,1,0]
]

def island_dfs_stack(grid):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    rows,cols = len(grid),len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 1:
                continue

            cnt += 1
            stack = [(row,col)]
            print(stack)
            while stack:
                x,y = stack.pop()
                grid[x][y] = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                        continue
                    stack.append((nx,ny))

    return cnt

result = island_dfs_stack(grid)
print(result)