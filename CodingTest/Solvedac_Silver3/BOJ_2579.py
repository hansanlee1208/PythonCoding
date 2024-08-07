import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
l_list = list(map(int, data[1:]))
# 계단을 한칸 올랐다면 다음은 반드시 두칸을 올라야함
# 1 -> 1 x, 1-> 2 , 2->2, 2->1 ㄱㄴ
# 처음 1번에서 1칸과 2번째 칸의 값 비교하여 큰 값으로
# 만약 1칸만 갔다면 다음은 반드시 2칸
if N == 1 :
    print(l_list[0])

else:
    dp = [0] * N
    dp[0] = l_list[0]
    dp[1] = l_list[0] + l_list[1]

    for i in range(2, N):
        dp[i] = max(dp[i-3]+ l_list[i-1]+l_list[i], dp[i-2] +l_list[i])

print(dp)