# https://www.acmicpc.net/problem/2884
H, M = map(int, input().split())
R_H, R_M = 0, 0

if H == 0:
    if M >= 45:
        R_H = 0
        R_M = M -45
    else:
        R_H = 23
        R_M = 60 - (45-M)
else:
    if M >= 45:
        R_H = H
        R_M = M -45
    else:
        R_H = H - 1
        R_M = 60 - (45-M)

print(R_H, R_M)