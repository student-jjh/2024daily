def binary_search(D,start,end,lst):
    mid = (start + end) // 2

    if start == end:
        return -1

    if lst[mid] == D:
        return mid
    elif lst[mid] > D:
        return binary_search(D,start,mid,lst)
    else:
        return binary_search(D,mid+1,end,lst)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,D = map(int,input().split())
    lst = list(map(int,input().split()))
    print(f"#{test_case} {binary_search(D,0,N,lst)+1}")
