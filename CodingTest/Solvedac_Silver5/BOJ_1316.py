def grp_check(text):
    S = set()
    is_true = 1
    for i in range(len(text)-1):
        S.add(text[i])
        if text[i+1] in S:
            if text[i] == text[i+1]:
                continue
            is_true = 0
            break
    return is_true

N = int(input())
cnt = 0
for _ in range(N):
    txt = input()
    cnt += grp_check(txt)
print(cnt)

