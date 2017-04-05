def min_max_number(A):
    #A is a list
    sorted_list= sorted(A)
    minimum = sorted_list[0]
    maximum = sorted_list[-1]
    if minimum==maximum:
        return len(A)
    else:
        return [minimum,maximum]
