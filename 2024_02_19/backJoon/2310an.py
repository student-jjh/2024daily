def dfs(room_num, my_money):
    global answer, visited
    if answer == 1:
        return;

    if rooms[room_num][0] == 'L':  # 레프리콘
        if rooms[room_num][1] > my_money:
            my_money = rooms[room_num][1]

    elif rooms[room_num][0] == 'T':  # 트롤
        if rooms[room_num][1] > my_money:
            return;
        else:
            my_money -= rooms[room_num][1]

    # print('2', room_num, my_money)
    if room_num == n - 1:
        answer = 1
        return;

    visited[room_num] = True
    for i in rooms[room_num][2]:
        if visited[int(i) - 1] == False:
            dfs(int(i) - 1, my_money)
    visited[room_num] = False


while True:
    n = int(input())
    if n == 0: break

    visited = [False] * n
    my_money = 0
    rooms = []
    answer = 0

    for _ in range(n):
        tmp = input().split()
        rooms.append([tmp[0], int(tmp[1]), tmp[2:-1]])

    dfs(0, 0)

    if answer == 0:
        print('No')
    else:
        print('Yes')