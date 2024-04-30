from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]  # 각 위치까지의 거리를 저장하는 배열

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dist[x][y] = 1  # 시작점의 거리는 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        i, j = queue.popleft()
        for xi, yj in directions:
            xx, yy = i + xi, j + yj
            if 0 <= xx < N and 0 <= yy < M:
                if grid[xx][yy] == 1 and not visited[xx][yy]:
                    visited[xx][yy] = True
                    dist[xx][yy] = dist[i][j] + 1
                    queue.append((xx, yy))
                    if (xx, yy) == (N-1, M-1):
                        return dist[xx][yy]  # 목표지점에 도달하면 즉시 반환

    return dist[N-1][M-1]  # 끝점의 거리 반환

print(bfs(0, 0))
