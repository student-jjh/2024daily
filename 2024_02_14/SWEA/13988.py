def binary_search(start,end,number):
    mid = (start + end) // 2
    if number == 1:
        return 1
    if start == end:
        return -1

    if mid*mid*mid == number :
        return mid

    elif mid*mid*mid < number:
        return binary_search(mid +1,end,number)
    else:
        return binary_search(start,mid,number)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())


    # 출력 준비
    print(f"#{test_case} {binary_search(0,N,N)}")