lst = []
check_set = set()

for _ in range(36):
    temp = input()
    check_set.add(temp)
    lst.append(list(temp))

# 같은거 두개 들어왔으면, 끝!!!
if len(check_set) != 36:
    print("Invalid")
else:
    lst.append(lst[0])
    def cal(A,B):
        if abs(ord(A[0]) - ord(B[0])) not in [1,2] or abs(int(A[1]) - int(B[1])) not in [1,2] or  abs(ord(A[0]) - ord(B[0])) + abs(int(A[1]) - int(B[1]))  != 3:
            return False

        return True
    bk = False
    for i in range(0,36):
        if cal(lst[i],lst[i+1]) == False:
            print("Invalid")
            bk = True
            break

    if bk == False:
        print("Valid")
