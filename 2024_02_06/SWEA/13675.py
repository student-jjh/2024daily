
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def recur(num,si):
    global cnt
    if sum(answer) > K:
        return
    if num == m:
        if sum(answer) == K:
            cnt +=1
        return

    for i in range(si,13):
        if visited[i] == False:
            visited[i] = True
            answer.append(i)
            recur(num+1,i+1)
            visited[i] = False
            answer.pop()



for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    temp = [i for i in range(1,13,1)]
    answer = []
    visited = [False for _ in range(13)]
    cnt = 0

    m = N
    recur(0,1)

    print(f"#{test_case} {cnt}")
