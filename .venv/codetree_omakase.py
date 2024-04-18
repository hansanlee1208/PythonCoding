import sys

class Query:
    def __init__(self, id, t, x, name):
        self.id = id
        self.t = t
        self.x = x
        self.name = name

input = sys.stdin.readline
#초밥 벨트 길이 L 명령의 수 Q
L, Q = map(int, input().rstrip().split())
queries = []
person_queries ={}
customers = set()
entry_time = {}
position = {}
exit_time = {}


for _ in range(Q):
    order, *data = input().rstrip().split()
    order = int(order)

    if order == 100:
        t = int(data[0])
        x = int(data[1])
        name = data[2]
        queries.append(Query(order, t,x,name))

        if name not in person_queries:
            person_queries[name] = [Query(order,t,x,name)]
        else:
            person_queries[name].append(Query(order,t,x,name))

    elif order == 200:
        t = int(data[0])
        x = int(data[1])
        name = data[2]
        n = int(data[3])
        queries.append(Query(order,t,x,name))
        customers.add(name)
        position[name] = x
        entry_time[name]= t
        exit_time[name] = -1

    #t 시각에 남은 사람수와 초밥수 출력
    elif order == 300:
        queries.append(Query(order,t,x,name))

    for name in customers:
        for pq in person_queries[name]:
            #사람이 초밥보다 먼저 도착
            if entry_time[name] < pq.t:
                add_time = (position[name]-pq.x +L) % L
                leave_time = pq.t + add_time
            else:
                sushi_pos = (entry_time[name]-pq.t +pq.x) % L
                add_time = (position[name] - sushi_pos + L) %L
                leave_time = entry_time + add_time
            queries.append(Query(150, leave_time, pq.x, name))
            exit_time[name] = max(exit_time[name],leave_time)

