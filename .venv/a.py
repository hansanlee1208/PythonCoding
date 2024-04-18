from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
for i in range(1, n):
    for j in range(m):
        if grid[i][j] == 'R':
            rx, ry = i, j
        if grid[i][j] == 'B':
            bx, by = i, j
        if grid[i][j] == 'O':
            hx, hy = i, j

def move(x, y, dx, dy):
    cnt = 0
    while grid[x+dx][y+dy] != '#':
        x += dx
        y += dy
        cnt += 1
        if (x, y) == (hx,hy):
            break
    return x, y, cnt

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by,1))
    visited[rx][ry][bx][by] = True
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    while queue:
        rx,  ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for dx, dy in directions:
            move_rx, move_ry, rcnt = move(rx, ry, dx, dy)
            move_bx, move_by, bcnt = move(bx, by, dx, dy)

            if (move_bx, move_by) != (hx, hy):
                if (move_rx, move_ry) == (hx, hy):
                    return depth
                if move_rx == move_bx and move_ry == move_by:
                    if rcnt > bcnt:
                        move_rx -= dx
                        move_ry -= dy
                    else:
                        move_bx -= dx
                        move_by -= dy

                if not visited[move_rx][move_ry][move_bx][move_by]:
                    visited[move_rx][move_ry][move_bx][move_by] = True
                    queue.append((move_rx, move_ry, move_bx, move_by, depth +1))
    return  -1

print(bfs(rx, ry, bx, by))