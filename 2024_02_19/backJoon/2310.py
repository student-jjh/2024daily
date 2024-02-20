def dfs(v,coin):
    global answer
    if answer == True:
        return
    if v == n:
        answer = True
        return


    for cost,node in graph[v]:
        # if visited[node] == False:
        if room_info[node] == "E":
            # visited[node] = True
            dfs(node,coin)
            # visited[node] = False
        elif room_info[node] == "L":
            if coin < cost:
                coin = cost
            # visited[node] = True
            dfs(node,coin)
            # visited[node] = False

        else:
            if coin > cost:
                coin -= cost
                # visited[node] = True
                dfs(node,coin)
                # visited[node] = False



while True:
    n = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n + 1)]
    room_info = [0]
    answer = False
    if n == 0 :
        break

    for i in range(1,n+1):
        lst = list(map(str,input().split()))
        if lst[0] == "E":
            room_info.append("E")
            for node in lst[2:-1]:
                graph[i].append((0,int(node)))

        elif lst[0] == "L":
            room_info.append("L")
            for node in lst[2:-1]:
                graph[i].append((int(lst[1]), int(node)))

        else:
            room_info.append("T")
            for node in lst[2:-1]:
                graph[i].append((int(lst[1]), int(node)))

    if room_info[1] == "T":
        print("No")
        continue
    elif room_info[1] == "L":
        dfs(1,graph[1][0][0])

    else:
        dfs(1,0)

    if answer == False:
        print("No")

    else:
        print("Yes")