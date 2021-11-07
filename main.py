def merge(*lists):
    full_list = []
    for i in lists:
        full_list += i
        full_list.sort()
    return full_list
print(merge(*lists))
