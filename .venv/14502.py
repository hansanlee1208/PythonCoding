import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def great_wall(grid):
    combinations_of_zeros = list(combinations(zero, 3))
    clean_position = 0
    for combination in combinations_of_zeros:
        copy_grid = copy.deepcopy(grid)
        for x,y in combination:
            copy_grid[x][y] = 1
        clean_area=bfs(virus, copy_grid)
        clean_position = max(clean_position, clean_area)

    return clean_position


def bfs(team, matrix):
    directions = [(0,1), (0, -1), (1,0), (-1, 0)]
    queue = deque(team)
    visited = [[False]*M for _ in range(N)]
    cnt =0

    for x, y in team:
        visited[x][y] = True

    while(queue):
        x,y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<= nx < N and 0<= ny < M and not visited[nx][ny] and matrix[nx][ny] == 0:
                matrix[nx][ny] =2
                visited[nx][ny] == True
                queue.append((nx,ny))

    return sum(row.count(0) for row in matrix)

N, M = map(int, input().split())

#0-빈 칸, 1-벽, 2-바이러스
grid = [list(map(int, input().rstrip().split())) for _ in range(N)]

#벽이랑 바이러스 있는 좌표를 미리 따놔야하나?
wall =set()
virus = set()
zero = set()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            wall.add((i,j))
        elif grid[i][j] == 2:
            virus.add((i, j))
        else:
            zero.add((i,j))

print(great_wall(grid))