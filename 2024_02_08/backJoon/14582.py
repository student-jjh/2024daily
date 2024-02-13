temp_1 = list(map(int,input().split()))
temp_2 = list(map(int,input().split()))

def isIt(lst1,lst2):
    s1,s2 = 0,0
    for i in range(9):
        s1 += lst1[i]
        if s1 > s2:
            return True
        s2 += lst2[i]

    return False

if isIt(temp_1,temp_2):
    print("Yes")
else:
    print("No")








