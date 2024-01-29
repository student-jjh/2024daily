N = int(input())

stack = []
temp = []
for_print = []
pointer = 0
i = 1
check = True

for _ in range(N):
    temp.append(int(input()))


while i != N+1 or pointer != N:
    if i < temp[pointer]:
        stack.append(i)
        for_print.append("+")
        i +=1

    elif i == temp[pointer]:
        for_print.append("+")
        for_print.append("-")
        pointer +=1
        i +=1

    else:
        a = stack.pop()
        if a == temp[pointer]:
            for_print.append("-")
            pointer +=1
        else:
            print("NO")
            check = False
            break


if check:
    for item in for_print:
        print(item)