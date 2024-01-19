from collections import deque

N, K = map(int, input().split())

count = 0
count_check = [0 for _ in range(123456)]


def bfs(N, K):
    if N == K:
        return 0
    queue = deque()

    queue.append(N)

    while queue:
        temp = queue.popleft()
        if (temp + 1) == K:
            count_check[temp + 1] = count_check[temp] + 1
            break

        else:

            if (temp + 1) <= 123455 and count_check[temp + 1] == 0:
                queue.append(temp + 1)
                count_check[temp + 1] = count_check[temp] + 1

        if (temp * 2) == K:
            count_check[temp * 2] = count_check[temp] + 1
            break
        else:

            if (temp * 2) <= 123455 and count_check[temp * 2] == 0:
                queue.append(temp * 2)
                count_check[temp * 2] = count_check[temp] + 1



        if temp - 1 == K:
            count_check[temp - 1] = count_check[temp] + 1
            break

        else:

            if 0<=(temp - 1) <= 123455 and count_check[temp - 1] == 0:
                queue.append(temp - 1)
                count_check[temp - 1] = count_check[temp] + 1

    return count_check[K]


print(bfs(N, K))