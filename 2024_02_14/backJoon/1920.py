N = int(input())
lst = list(map(int,input().split()))
lst.sort()
M = int(input())
to_find = list(map(int,input().split()))



def binary_search(D,start,end,lst):
    mid = (start + end) // 2

    if start == end:
        return -1

    if lst[mid] == D:
        return mid
    elif lst[mid] > D:
        return binary_search(D,start,mid,lst)
    else:
        return binary_search(D,mid+1,end,lst)

for number in to_find:
    if binary_search(number,0,N,lst) != -1:
        print(1)

    else:
        print(0)