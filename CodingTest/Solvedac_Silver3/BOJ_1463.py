# num = int(input())
#
# cache = {1:0, 2:1, 10:3}
# def dp(n):
#     if n in cache:
#         return cache[n]
#     cnt = 1+ min(dp(n//3)+ n%3, dp(n//2) + n%2)
#     cache[n]= cnt
#     return cnt
#
# print(dp(num))

n = int(input())
d = [0]*(n+1)
for i in range(2, n+1):
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

print(d[n])