T = int(input())
def insertion(N):
    count = 0
    for i in range(1,len(N)):
        temp = N[i]
        j = i
        while j > 0 and N[j-1] > temp:
            N[j] = N[j-1]
            j -=1
        N[j] = temp
        count += (i-j)
    return count
for i in range(T):
    temp_list = list(map(int,input().split()))[1:]
    print(f"{i+1} {insertion(temp_list)}")

