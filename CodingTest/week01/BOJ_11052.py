N = int(input())

l_list = list(map(int, input().split()))

N_list = l_list[:]

for i in range(N):
    for j in range(i):
        N_list[i] = max(N_list[i], N_list[i-j-1] + l_list[j])
        #점화식 확인
        # print(i, N_list[i])
print(N_list[N-1])