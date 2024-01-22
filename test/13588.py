T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())


    temp_list = list(map(int,input().split()))
    temp =[]
    for i in range(N-M+1):
        temp.append(sum(temp_list[i:i+M]))

    temp.sort()
    print(temp)
    print(f"#{test_case} {temp[-1] - temp[0]}")