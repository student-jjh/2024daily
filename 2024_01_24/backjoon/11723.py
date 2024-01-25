import sys
input =sys.stdin.readline


S = set()

M = int(input())

for i in range(M):
    temp = input().strip()

    if temp == "all":
        S = {str(i) for i in range(1,21)}

    elif temp == "empty":
        S = set()

    else:
        commend, number = map(str, temp.split())
        if commend == "add":
            S.add(number)
        elif commend == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)

        elif commend == "remove":
            S.discard(number)
        elif commend == "check":
            if number in S:
                print(1)
            else:
                print(0)



