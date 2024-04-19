def caltime(num, lst):
    stairtime = stairlst[num][2]
    stairpeople = [0,0,0]
    lst.sort()
    for idx in range(len(lst)):
        kidx = idx%3
        k = lst[idx]
        if stairpeople[kidx] < k:
            stairpeople[kidx] = k+stairtime
        else:
            stairpeople[kidx] += stairtime
    return max(stairpeople)

def makecase(idx, lst, lst2):
    global answer
    if idx == len(peoplelst):
        thistime = max(caltime(0, lst), caltime(1, lst2))
        answer = min(answer, thistime)
        return

    pi, pj = peoplelst[idx]
    ai, aj, _ = stairlst[0]
    bi, bj, _ = stairlst[1]
    dist1 = abs(ai-pi) + abs(aj-pj)
    dist2 = abs(bi-pi) + abs(bj-pj)

    makecase(idx+1, lst+[dist1], lst2)
    makecase(idx+1, lst, lst2+[dist2])
T = 1
for tc in range(1, T+1):
    ### 입력 받기
    N = 5
    arr = [list(map(int, input().split())) for _ in range(N)]
    peoplelst, stairlst = [], []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: peoplelst.append((i,j))
            elif 2<=arr[i][j]<=10: stairlst.append((i,j, arr[i][j]))
    answer = 1e9
    makecase(0, [], [])
    print(f"#{tc} {answer+1}")