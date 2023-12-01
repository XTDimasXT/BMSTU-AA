def block_sort(arr):
    block_size = 10
    blocks = []

    i = 0
    while i < len(arr):
        block = []
        j = i
        while j < i + block_size and j < len(arr):
            block.append(arr[j])
            j += 1
        block.sort()
        blocks.append(block)
        i += block_size

    arr_ind = 0
    while blocks:
        min_ind = 0
        for i in range(1, len(blocks)):
            if blocks[i][0] < blocks[min_ind][0]:
                min_ind = i
        
        arr[arr_ind] = blocks[min_ind][0]
        arr_ind += 1
        blocks[min_ind].pop(0)

        if not blocks[min_ind]:
            blocks.pop(min_ind)
            
    return arr


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