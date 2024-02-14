N,M = map(int,input().split())

tree_list = list(map(int,input().split()))
answer = 0
for_answer = 0
def binary_search(start,end,number):
    global answer
    mid = (start + end) // 2

    if start == end:
        return

    temp_list = [max(0,i-mid) for i in tree_list]
    if sum(temp_list) == number:
        answer = mid

    elif sum(temp_list) < number:
        return binary_search(start,mid,number)

    else:
        answer = mid
        return binary_search(mid+1,end,number)

binary_search(0,max(tree_list),M)
print(answer)
