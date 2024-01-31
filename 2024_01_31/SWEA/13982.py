from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())

    wait_list = deque(list(map(int,input().split())))
    running_list = deque()

    cnt = 0

    while cnt < N:
        cnt += 1
        running_list.append([wait_list.popleft(),cnt])


    while running_list:
        temp = running_list.popleft()

        time_temp = temp[0] // 2
        if time_temp == 0:
            if wait_list != deque():
                cnt +=1
                running_list.append([wait_list.popleft(),cnt])
            else:
                cnt -=1

        else:
            running_list.append([time_temp,temp[1]])

        if len(running_list) == 1:
            break

    print(f"#{test_case} {running_list.popleft()[1]}")
