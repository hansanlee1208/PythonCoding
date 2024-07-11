N = int(input())
cnt = 0
for _ in range(N):
    checked = set()
    is_group_word = True
    word = input().strip()
    for  i in range (len(word)):
        if i > 0 and word[i] == word[i-1]:
            continue
        if word[i] in checked:
            is_group_word = False
            break
        checked.add(word[i])
    cnt += is_group_word

    # Word = input()
    # bow = []
    # if len(Word) == 1:
    #     cnt += 1
    # else:
    #     for j in range(len(Word)):
    #         if j == 0:
    #             bow.append(Word[0])
    #         elif j > 0:
    #             if Word[j-1] == Word[j]:
    #                 bow.append(Word[j])
    #                 if j == len(Word)-1:
    #                     cnt += 1
    #             elif Word[j-1] != Word[j]:
    #                 if Word[j] not in bow:
    #                     if j == len(Word)-1:
    #                         cnt += 1
    #                     else:
    #                         bow.append(Word[j])
    #                 elif Word[j] in bow:
    #                     break
print(cnt)
# def grp_word_check(word):
#     for i in range(word.length)
