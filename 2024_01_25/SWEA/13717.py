
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B  = map(str,input().split())
    cnt = 0
    i = 0
    while i < len(A):
        if A[i:i+len(B)] == B :
            i += len(B)
        else:
            i+= 1

        cnt +=1

    print(f"#{test_case} {cnt}")