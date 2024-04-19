#위는 시간 초과 코드.
#입력과 출력이 어느 정도를 넘어간다면 sys 함수 사용하도록.
N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
arr.sort()

for i in arr:
    print(i)

#아래 방법이 훨씬 빠르다. 메모리도. 속도도
#import sys
#입력을 한번에 읽어준다.
# input = sys.stdin.read
#data = input().split()
#N = int(data[0])
# arr = list(map(int, data[1:]))
# arr.sort()
#print('\n'.join(map(str,arr)))
