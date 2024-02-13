
def recur(month,money):
    global answer
    if money > answer:
        return
    if month >=12:
        if money < answer:
            answer = money
        return


    recur(month+1,min(money + one*plan[month],money + months))
    recur(month + 3, money + qua)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 각 이용권 별 금액 입력
    one,months,qua,year = map(int,input().split())
    plan = list(map(int,input().split()))
    answer = year
    recur(0,0)
    print(f"#{test_case} {answer}")