import sys

input = sys.stdin.readline

N, M, P, C, D = map(int, input().rstrip().split())
R_r, R_c = map(int, input().rstrip().split())
santa_position = {}
santa = set()
point = {}
for _ in range(P):
    num, S_r, S_c = map(int,input().rstrip().split())
    santa_position[num] = (S_r, S_c)
    point[num]=0
    santa.add(num)


