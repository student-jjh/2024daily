def merge(A,B):
    global cnt
    if B[-1] < A[-1]:
        cnt +=1
    i,j = 0,0
    for_return = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            for_return.append(A[i])
            i+=1
        else:
            for_return.append(B[j])
            j+=1
    for_return += A[i:]
    for_return += B[j:]

    return for_return

def merge_sort(lst):
    middle = len(lst) //2
    if len(lst) == 1:
        return lst

    else:
        return merge(merge_sort(lst[:middle]),merge_sort(lst[middle:]))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    lst = merge_sort(lst)
    print(f"#{test_case} {lst[N//2]} {cnt}")
    # print(*lst[N//2])