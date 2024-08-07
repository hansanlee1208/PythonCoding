def worm(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            worm(i)

N = int(input())
k = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(k):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


worm(1)
cnt = visited.count(True)-1
print(cnt)