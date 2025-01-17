# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(smallest_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
               smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    complete = False
    while not complete:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i -1]
                arr[i - 1] = temp
                swapped = True
        if not swapped:
            complete = True
    return arr

# STRETCH: implement the Count Sort function below
#NOT MY CODE. JUST WANTED TO HAVE THIS AS A REFERENCE MOVING FORWARD
def count_sort( arr, maximum=-1 ):
    if maximum > 0:
        counts = [0] * maximum
    else:
        counts = []

    for item in arr:
        if item < 0:
            return 'negative numbers not allowed'
        if maximum < 0 and item + 1 > len(counts):
            extend_count = item + 1 - len(counts)
            counts = counts + [0] * extend_count
        counts[item] += 1

    arr = []

    for index, item in enumerate(counts):
        if item:
            arr = arr + [index] * item

    return arr
