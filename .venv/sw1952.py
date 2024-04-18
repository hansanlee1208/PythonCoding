# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# def dfs(month, cost):
#     if month > 12:
#         global min_cost
#         min_cost = min(min_cost, cost)
#         return
#
#     if year_list[month] ==0:
#         dfs(month+1, cost)
#     else:
#         dfs(month +1, cost+year_list[month]*d_p)
#         dfs(month+1, cost +m_p)
#         dfs(month+3, cost+m_3_p)
#
# for test_case in range(1, T + 1):
#     d_p, m_p, m_3_p, y_p = map(int, input().split())
#     year_list = [0] + list(map(int, input().split()))
#
#     min_cost = y_p
#     dfs(1,0)


d_p, m_p, m_3_p, y_p = map(int, input().split())

month_list = [0]+list(map(int, input().split()))
min_price = y_p
dfs(1, 0)

def dfs(month, price):
    if month>12:
        global min_price
        price = min(min_price, price)
        return

    if month_list[month] == 0:
        dfs(month+1, price)
    else:
        dfs(month+1, month_list[month]*d_p)
        dfs(month+1, m_p)
        dfs(month+3, m_3_p)
