def block_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = block_sort(arr[:mid])
        right = block_sort(arr[mid:])
        
        return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result


def quick_sort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    
    else:
        return arr


def selection_sort(arr):
    size = len(arr)

    for ind in range(size):
        min_ind = ind
 
        for j in range(ind + 1, size):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[ind], arr[min_ind] = arr[min_ind], arr[ind]

    return arr