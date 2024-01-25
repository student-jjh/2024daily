from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    move = [0 for _ in range(201)]
    moves = []
    for i in range(N):
        s,e = map(int,input().split())
        if s % 2 == 0 :
            s -=1
        s = s//2

        if e % 2 ==0 :
            e-= 1
        e =e // 2
        mn = min(e,s)
        mx = max(s,e)
        for j in range(mn,mx+1):
            move[j] +=1


    print(f"#{test_case} {max(move)}")