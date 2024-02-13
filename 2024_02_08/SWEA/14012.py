# 그냥 간단하게 백트레킹으로 이거 쓸꺼야 안쓸꺼야... 판단..?
# 근데 베터리 양보다 남은 정류장이 적으면 걍 ㄱ로 만들면 ...?
def recur(bettery,cnt,si):
    global answer
    # 가지치기
    if cnt > answer :
        return
    # 종료 조건
    if N-si <= bettery:
        if cnt < answer:
            answer = cnt
        return

    for i in range(si,min(bettery+si,N)):
        recur(batterys[i+1],cnt +1, i+1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    #입력 받고... 필요에 따라 나누기
    temp = list(map(int,input().split()))
    N = temp[0] -1
    batterys = temp[1:]
    answer = 51
    visited = [False for _ in range(N)]

    recur(batterys[0],0,0)
    print(f"#{test_case} {answer}")