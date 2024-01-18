temp =[]
_max = 0
for i in range(5):
    temp_lst = list(input())
    if len(temp_lst) > _max:
        _max =len(temp_lst)
    temp.append(temp_lst)

for j in range(_max):
    for k in range(5):
        try:
            print(temp[k][j],end="")
        except:
            pass