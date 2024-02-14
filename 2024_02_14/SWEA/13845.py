def merge(A,B):
    if A[0][0] == B[0][0]:
        if A[0][1] < B[0][1]:
            return A
        else:
            return B
    else:
        if (A[0][0] == 1 and B[0][0] == 2) or (A[0][0] == 2 and B[0][0] == 3) or (A[0][0] == 3 and B[0][0] ==1):
            return B
        else:
            return A

def rocksipa(lst):
    if len(lst) % 2 == 0:
        mid = len(lst) //2
    else:
        mid = (len(lst) +1) //2
    if len(lst) == 1:
        return lst

    else:
        return merge(rocksipa(lst[mid:]),rocksipa(lst[:mid]))




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst = [[lst[i],i+1] for i in range(len(lst))]
    answer = rocksipa(lst)
    print(f"#{test_case} {answer[0][1]}")