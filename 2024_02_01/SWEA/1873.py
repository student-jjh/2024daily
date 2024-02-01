

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    field = []
    for i in range(N):
        temp = list(input())
        if "^" in temp:
            start = [i,temp.index("^")]
        if "v" in temp:
            start = [i, temp.index("v")]
        if "<" in temp:
            start = [i, temp.index("<")]
        if ">" in temp:
            start = [i, temp.index(">")]
        field.append(temp)

    order_num = int(input())
    orders = input()
    i,j = start[0],start[1]
    for order in orders:
        if order =="U":
            field[i][j] = "^"
            if i-1 >=0 and field[i-1][j] == ".":
                field[i-1][j] = "^"
                field[i][j] = "."
                i,j = i-1,j
        elif order =="D":
            field[i][j] = "v"
            if i+1 < N and field[i+1][j] == ".":
                field[i+1][j] = "v"
                field[i][j] = "."
                i,j = i+1,j
        elif order =="L":
            field[i][j] = "<"
            if j-1 >= 0 and field[i][j-1] == ".":
                field[i][j-1] = "<"
                field[i][j] = "."
                i,j = i, j-1
        elif order =="R":
            field[i][j] = ">"
            if j +1 < M and field[i][j+1] == ".":
                field[i][j+1] = ">"
                field[i][j] = "."
                i,j = i, j +1
        elif order == "S":
            if field[i][j] == "^":
                for k in range(i-1,-1,-1):
                    if field[k][j] == "*":
                        field[k][j] = "."
                        break
                    elif field[k][j] == "#":
                        break

            elif field[i][j] == "v":
                for k in range(i+1,N):
                    if field[k][j] == "*":
                        field[k][j] = "."
                        break
                    elif field[k][j] == "#":
                        break
            elif field[i][j] == "<":
                for k in range(j -1,-1, -1):
                    if field[i][k] == "*":
                        field[i][k] = "."
                        break
                    elif field[i][k] == "#":
                        break
            elif field[i][j] == ">":
                for k in range(j + 1, M):
                    if field[i][k] == "*":
                        field[i][k] = "."
                        break
                    elif field[i][k] == "#":
                        break
    print(f"#{test_case}",end = " ")
    for line in field:
        print("".join(line))





