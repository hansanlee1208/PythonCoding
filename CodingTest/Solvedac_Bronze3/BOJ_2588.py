#백준 브론즈 3 2588 문제
# https://www.acmicpc.net/problem/2588
A = int(input())
B = int(input())

B_1 = B % 10
B_2 = B // 10 % 10
B_3 = B // 100

R_1 = A*B_1
R_2 = A*B_2
R_3 = A*B_3

print(R_1)
print(R_2)
print(R_3)
print(R_1+ R_2*10 + R_3*100)

A = int(input())
B = input()

R_1 = A * int(B[2])
R_2 = A * int(B[1])
R_3 = A * int(B[0])

print(R_1)
print(R_2)
print(R_3)
print(R_1+ R_2*10 + R_3*100)
