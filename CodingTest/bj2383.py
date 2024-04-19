EMPTY = 0
PERSON = 1


def rec(depth):
    global ans
    if depth == p:
        # 0/1 번 계단까지 사람들이 도착하는 시간대
        to_stair = [[0, 0, 0], [0, 0, 0]]

        for i in range(p):
            # q에는 i번째 사람이 0/1 계단을 선택하는지가 들어있음.
            which = q[i]
            # dist[i][0] : i번째 사람의 0계단까지의 거리
            to_stair[which].append(dist[i][which])

        tmp = 0
        for i in range(2):
            s1 = to_stair[i]
            stair_length = stairs[i][2]
            s1.sort()
            for k in range(3, len(s1)):
                s1[k] = max(s1[k] + stair_length, s1[k - 3] + stair_length)  # +1 붙여?######
            tmp = max(tmp, max(s1))
        ans = min(ans, tmp)
        return

    q.append(0)
    rec(depth + 1)
    q.pop()
    q.append(1)
    rec(depth + 1)
    q.pop()


T = int(input())
for tc in range(1, T + 1):
    ans = int(10e9)

    # 한 변의 길이 N(4~10)
    N = int(input())
    # 0 빈칸 1 사람, 2이상 계단 입구(계단의 길이)
    arr = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []  # 계단의 번호는 인덱스, 계단의 좌표와 계단 길이

    for i in range(N):
        for j in range(N):
            if arr[i][j] == EMPTY:
                continue
            elif arr[i][j] == PERSON:
                people.append((i, j))
            else:
                stairs.append((i, j, arr[i][j]))

    # 사람별로 0, 1번째 계단까지의 거리 +1 (그 시간부터 계단 내려갈 수 있음)
    dist = []
    for pi, pj in people:
        tmp = []
        for i in range(2):
            si, sj, _ = stairs[i]
            tmp.append(abs(si - pi) + abs(sj - pj) + 1)
        dist.append(tmp)

    p = len(people)
    q = []
    rec(0)

    print(f'#{tc} {ans}')