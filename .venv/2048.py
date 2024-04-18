import sys

input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().rstrip().split())) for _ in range(N)]

def rotate_block(block):
    return list(zip(*block[::-1]))

def upper(grid):
    new_grid = grid.copy()

    for j in range(N):
        non_zero = [new_grid[i][j] for i in range(N) if new_grid[i][j] != 0]
        i=1
        for i in range(1, len(non_zero)):
            if non_zero[i] == non_zero[i-1]:
                non_zero[i-1] *= 2
                non_zero[i] =0
        non_zero = [num for num in non_zero if num != 0]
        for i in range(N):
            new_grid[i][j]  = non_zero[i] if i < len(non_zero) else 0
    return new_grid

def dfs(grid, depth):
    if depth == 5:
        return max(map(max, grid))
    max_val = 0
    for _ in range(4):
        new_matrix = upper(grid)
        max_val = max(max_val, dfs(new_matrix, depth+1))
        grid = rotate_block(grid)
    return max_val

print(dfs(grid, 0))

