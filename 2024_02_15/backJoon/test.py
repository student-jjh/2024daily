N = int(input())
lst = list(map(str,input().split()))

def check(lst,temp_lst,num):
    temp_str = ""
    for i in range(num-1):
        temp_str+=str(temp_lst[i])
        temp_str+=lst[i]
    temp_str+=str(temp_lst[num-1])
    return eval(temp_str)




visited = [False for _ in range(10)]
is_print = False
temp_lst = []
def recur(num):
    global is_print
    if is_print == True:
        return
    if num >=3 and check(lst,temp_lst,num) == False:
        return
    if num == N+1:
        if check(lst,temp_lst,num):
            print("".join(list(map(str,temp_lst))))
            is_print = True
        return

    for i in range(10):
        if visited[i] == False:
            temp_lst.append(i)
            visited[i] = True
            recur(num + 1)
            visited[i] = False
            temp_lst.pop()

def recur_reverse(num):
    global is_print
    if is_print == True:
        return
    if num >=3 and check(lst,temp_lst,num) == False:
        return
    if num == N+1:
        if check(lst,temp_lst,num):
            print("".join(list(map(str,temp_lst))))
            is_print = True
        return

    for i in range(9,-1,-1):
        if visited[i] == False:
            temp_lst.append(i)
            visited[i] = True
            recur_reverse(num + 1)
            visited[i] = False
            temp_lst.pop()

recur_reverse(0)
is_print = False
recur(0)