# def fibonacci(N):
#     if N == 0:
#         cnt[0] += 1
#         return
#     elif N == 1:
#         cnt[1] += 1
#         return
#     else :
#         fibonacci(N-1)
#         fibonacci(N-2)
#         return

import sys
input = sys.stdin.readline

T = int(input())

cnt = {0:[1,0], 1:[0,1]}

for i in range(2,41):
    cnt[i] = [cnt[i-1][1], sum(cnt[i-1])]
for _ in range(T):
    N = int(input())
    print(cnt[N][0], cnt[N][1])