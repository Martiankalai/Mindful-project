def uniq_list(num):
    unique_list = []
    seen_set = set()
    for num in list:
        if num not in seen_set:
            unique_list.append(num)
            seen_set.add(num)
    return unique_list


num = [1, 2, 3, 2, 3, 4, 5]
print("Unique elements is:", uniq_list(num))
