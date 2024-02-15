N = input()

if "7" in N:
    if int(N) % 7 == 0:
        print(3)

    else:
        print(2)
else:
    if int(N) % 7 == 0:
        print(1)

    else:
        print(0)