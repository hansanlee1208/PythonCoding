# def vitonic_arr(l_list, N):
#     cre = [1 for _ in range(N)]
#     for i in range(N):
#         for j in range(i):
#             if l_list[i] > l_list[j]:
#                 cre[i] = max(cre[i], cre[j]+1)
#     return cre

N = int(input())
N_list = list(map(int, input().split()))
reverse_list = N_list[::-1]

incre = [1 for _ in range(N)]
decre = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if N_list[i] > N_list[j]:
            incre[i] = max(incre[i], incre[j]+1)
        if reverse_list[i] > reverse_list[j]:
            decre[i] = max(decre[i], decre[j] +1)

result = [0 for _ in range(N)]

for i in range(N):
    result[i] = incre[i] + decre[N-i-1] -1

print(max(result))