X = int(input())
O_X = X
line = 0
S = 0
while (O_X>0):
    line+=1
    S += line
    O_X -=line


# 이렇게 나온 line 값이 몇번째 줄에 있는 수인지를 알 수 있는 키
#  F는 그 라인의 첫 값
# 짝수 줄일때랑 홀수 줄 일때의 차이
K = S-X #뒤에서 몇번째 수인지
A = line -K
B = 1+K
if line %2 == 0:
    print(f'{A}/{B}')
else:
    print(f'{B}/{A}')