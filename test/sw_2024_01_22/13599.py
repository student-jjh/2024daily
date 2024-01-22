
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    temp_list= list(map(int,input().split()))

    count = 0

    for i in range(2,N):
        temp = temp_list[i-2:i]+temp_list[i+1:i+3]

        if temp_list[i] > max(temp):
            count += temp_list[i] - max(temp)

    print(f"#{test_case} {count}")