N = int(input())

grid = [list(map(int, input().strip())) for _ in range(N)]
ad = 0
for l in grid:
    ad += sum(l)
k = N//2
for i in range(k):
    ad -= sum(grid[i])
    ad -= sum(grid[N-i-1])
    y = k-i
    for j in range(k):
        ad += grid[j][y]
        ad += grid[N-j-1][y]
        if i != 0:
            ad+= grid


    #N =3  i = 0 (0,0)(0,2)(2,0)(2,2)
    #N = 5 i = 0,1 (0,0)(0,1)(0,3)(0,4) (1,0)(1,4)  (3,0)(3,4)  (4,0)(4,1)(4,3)(4,4)
    #N = 7 i = 0,1,2,3 (0,0)



#N =1 (0,0)
#N = 3 (1,1) 시작 상하좌우
#N = 5 (2,2) 시작  상하좌우