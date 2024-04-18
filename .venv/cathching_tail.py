# import sys
# input = sys.stdin.readline
#
# def find_priority(jump_cnt,x, y,pid):
#
#
# def race_start():
#
#
# def move_dist():
#     global dict
#     dict[str(pid_t)] = L
#
# Q = int(input())
# rabitdist = {}
# rabitnum = {}
# rabitlist = []
#
# max_val = -float('inf')
#
# for _ in range(Q):
#     l_list = list(map(int, input().rstrip().split()))
#
#     if l_list[0] == 100:
#         N = l_list[1]
#         M = l_list[2]
#         P = l_list[3]
#         dict = {str(l_list[4+i]) : l_list[5+i] for i in range(P)}
#         rabitscore = [0]*P
#         ROW = [s for s in range(N)] + [s for s in range(N-2, 0 , -1)]
#
#     elif l_list[0] == 200:
#         K = l_list[1]
#         S = l_list[2]
#         race_start(K, S)
#
#     elif l_list[0] == 300:
#         pid_t = l_list[1]
#         L = l_list[2]
#         move_dist(pid_t, L)
#
#     elif l_list[0] == 400:
#         print(max_val)
import heapq, sys

input = sys.stdin.readline
Q = int(input())
rabitdist = {}
rabitnum = {}
rabitlist = []

for _ in range(Q):
    order, *data = map(int, input().rstrip().split())
    if order == 100:
        N, M, P, *rabitdata = data
        rabitscore = [0]*P
        ROW = [s for s in range(N)] +[s for s in range(N-2,0,-1)]
        COL = [s for s in range(M)] +[s for s in range(M-2,0,-1)]
        for i in range(0, P):
            num = rabitdata[i*2]
            rabitdist[num] = rabitdata[i*2+1]
            rabitnum[num] = i
            heapq.heappush(rabitlist, (0,0,0,0,num))
    elif order == 200:
        K, S = data
        newrabit = []
        for _ in range(K):
            jumpcnt, hap, i, j, num = heapq.heappop(rabitlist)
            jumpdist = rabitdist[num]
            poslst = []
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ci, cj = ROW[(i+di *jumpdist) % (len(ROW))]
