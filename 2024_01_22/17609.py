T = int(input())
def is_pal_sub(st):
    for i in range(len(st)//2):
        if st[i] != st[-1-i]:
            return False
    return True
def is_pal(st):
    is_p = True
    for i in range(len(st)//2):
        if st[i] != st[-1-i]:
            is_p = False
            break
    if is_p:
        return 0

    else:
        for i in range(len(st)):
            new_st = st[0:i] + st[i+1:]
            if is_pal_sub(new_st):
                return 1

        return 2

for i in range(T):
    temp = input()
    print(is_pal(temp))
