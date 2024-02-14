N = int(input())

lst = []

for _ in range(N):
    lst.append(int(input()))

def quick_sort(start,end,lst):
    if start == end :
        return
    middle = (start + end) // 2

    while start < end:
        while lst[start] < lst[middle]:
            start +=1

        while lst[end] > lst[middle]:
            end -=1

        lst[start],lst[end] = lst[end],lst[start]

    quick_sort(start,middle,lst)
    quick_sort(middle,end,lst)

quick_sort(0,len(lst)-1,lst)




# def merge(A,B):
#     i,j = 0,0
#     for_return = []
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             for_return.append(A[i])
#             i+=1
#         else:
#             for_return.append(B[j])
#             j+=1
#     for_return += A[i:]
#     for_return += B[j:]
#
#     return for_return
#
# def merge_sort(lst):
#     middle = len(lst) //2
#     if len(lst) == 1:
#         return lst
#
#
#     else:
#         return merge(merge_sort(lst[:middle]),merge_sort(lst[middle:]))

for i in lst:
    print(i)
