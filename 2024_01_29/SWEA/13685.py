T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sr = input()
    stack = []
    cnt = 0
    i = 0
    while i < len(sr)-1:
        if sr[i:i+2] == "()":
            cnt += len(stack)
            i+=2

        elif sr[i] == "(":
            stack.append(sr[i])
            i+=1

        else:
            stack.pop()
            cnt +=1
            i+=1
    if i == len(sr)-1:
        cnt +=1
    print(f"#{test_case} {cnt}")

