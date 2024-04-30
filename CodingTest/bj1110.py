def add_cycle(num):
    return (num % 10)*10 + ((num//10)+(num % 10)) % 10

N = int(input())
cnt = 0
dnum = N

while True:
    cnt += 1
    dnum = add_cycle(dnum)
    if dnum == N:
        break
print(cnt)