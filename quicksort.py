temp = [1,363,524,22,125,462,5]

def quick_sort(lst):

    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    temp = lst[1:]


    left_side = [x for x in temp if x < pivot]
    right_side = [x for x in temp if x >=pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(temp))