def bubble_sort(lst):
    for i in range(0, len(lst), 1):
        for j in range(len(lst)-1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    temp = list(map(int, input().split()))

    temp = bubble_sort(temp)

    temp = list(map(str, temp))
    sr = " ".join(temp)

    print(f"#{test_case} {sr}")