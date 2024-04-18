N = int(input())
two_d_arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(matrix):
    return list(zip(*matrix[::-1]))

def upper(matrix):
    new_matrix = matrix.copy()  # 행렬 복사
    for j in range(N):
        # 0이 아닌 항목만 남깁니다.
        non_zero = [new_matrix[i][j] for i in range(N) if new_matrix[i][j] != 0]
        # 위로 이동하면서 합치기
        i = 0
        for i in range(len(non_zero)):
            if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
                non_zero[i] *= 2
                non_zero[i + 1] = 0
        # 다시 0이 아닌 항목만 남깁니다.
        non_zero = [num for num in non_zero if num != 0]
        # 행렬 업데이트
        for i in range(N):
            new_matrix[i][j] = non_zero[i] if i < len(non_zero) else 0
    return new_matrix

def dfs(matrix, depth):
    if depth == 5:
        return max(map(max, matrix))
    max_val = 0
    for _ in range(4):  # 네 방향 모두 탐색
        new_matrix = upper(matrix)
        max_val = max(max_val, dfs(new_matrix, depth + 1))
        matrix = rotate(matrix)  # 다음 방향으로 회전
    return max_val

print(dfs(two_d_arr, 0))
