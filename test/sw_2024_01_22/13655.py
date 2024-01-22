T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    dump = int(input())

    temp = list(map(int,input().split()))

    for i in range(dump):
        temp.sort()
        temp[0] += 1
        temp[-1] -= 1
    temp.sort()
    answer = max(temp) - min(temp)
    print("#", test_case, " ", answer, sep='')

for i in range(1, T + 1):
    M = int(input())
    arr = list(map(int, input().split()))
    for j in range(M):
        maxVal = max(arr)
        minVal = min(arr)
        minIdx = arr.index(minVal)
        maxIdx = arr.index(maxVal)
        arr[minIdx] += 1
        arr[maxIdx] -= 1
    answer = max(arr) - min(arr)
    print("#", i, " ", answer, sep='')