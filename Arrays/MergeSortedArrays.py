def merge_sorted_arrays(array1, array2):
    arr1_len = len(array1)
    arr2_len = len(array2)
    sorted_list = []
    i = 0
    j = 0
    if not array1:
        return array2
    elif not array2:
        return array1
    else:
        while i < arr1_len and j < arr2_len:
            if array1[i] < array2[j]:
                sorted_list.append(array1[i])
                i += 1
            else:
                sorted_list.append(array2[j])
                j += 1
        while i < arr1_len:
            sorted_list.append(array1[i])
            i += 1
        while j < arr2_len:
            sorted_list.append(array2[j])
            j += 1
        return sorted_list


print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))
