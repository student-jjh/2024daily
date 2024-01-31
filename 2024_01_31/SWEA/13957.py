from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    temp_list = list(map(int,input().split()))

    queue = deque(temp_list)

    while True:
        break_point = False
        for i in range(1,6):
            check = queue.popleft()
            check -= i
            if check <= 0:
                queue.append(0)
                break_point = True
                break
            else:
                queue.append(check)
        if break_point == True:
            break

    print(f"#{test_case}",end = " ")
    while queue:
        print(queue.popleft(),end=' ')
    print()



