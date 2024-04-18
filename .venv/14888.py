from itertools import permutations

# 입력을 받습니다.
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값을 초기화합니다.
max_value = -float('inf')
min_value = float('inf')

def dfs(idx, result, add, sub, mul, div):
    global max_value
    global  min_value

    if idx == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    if add:
        dfs(idx+1, result + numbers[idx], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, result - numbers[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, result * numbers[idx], add, sub, mul-1, div)
    if div:
        if result<0:
            dfs(idx+1, -(-result//numbers[idx]), add, sub, mul, div-1)
        else:
            dfs(idx+1, result// numbers[idx], add, sub, mul, div-1)

dfs(1, numbers[0], add, sub, mul, div)
# 최댓값과 최솟값을 출력합니다.
print(max_value)
print(min_value)
