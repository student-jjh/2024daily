def recur(num,si):
    global answer
    global answers
    if answers > answer:
        return

    elif B<= answers < answer:
            answer = answers
            return

    if num == m:
        if B<= answers < answer:
            answer = answers
        return

    for i in range(si,N):
        if visited[i] == False:
            visited[i] = True
            answers += persons[i]
            recur(i+1,num+1)
            visited[i] = False
            answers -= persons[i]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, B = map(int,input().split())

    persons = list(map(int,input().split()))
    visited = [False for _ in range(N+1)]

    answer = sum(persons)
    answers = 0

    for i in range(1,N+1):
        m = i
        recur(0,0)
        if answer == B:
            break
    print(f"#{test_case} {answer-B}")


