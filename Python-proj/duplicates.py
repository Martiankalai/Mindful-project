arr = [1, 7, 12, 3, 4, 2]


def duplicate(arr):
    lis = []
    for ele in arr:
        if ele not in lis:
            lis.append(ele)
        else:
            return True
    return False


print(duplicate(arr))
