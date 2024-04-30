N = int(input())

sc_list = list(map(int, input().split()))
new_list = []
max_sc = max(sc_list)

for sc in sc_list:
    sc = sc/max_sc*100
    new_list.append(sc)

avg_new_list = sum(new_list)/N

print(avg_new_list)
