testArr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    indexA = 0
    indexB = 0
    for i in range(0, elements):
        if indexA >= len(arrA):
            merged_arr[i] = arrB[indexB]
            indexB += 1
        elif indexB >= len(arrB):
            merged_arr[i] = arrA[indexA]
            indexA += 1
        elif arrA[indexA] < arrB[indexB]:
            merged_arr[i] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[i] = arrB[indexB]
            indexB += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left,right)
        print(arr)

    return arr

print(merge_sort(testArr))
# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
    # # TO-DO

    # return arr

# def merge_sort_in_place(arr, l, r):
    # # TO-DO

    # return arr

# NOT MY CODE. JUST WANTED TO SEE HOW IT WAS DONE FOR REFERENCE GOING FORWARD
import random

def merge_sort(xs):
    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0,len(xs),unit *2):
            l,r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            p,q = l, mid
            while p < mid and q < r:
                if xs[p] < xs[q]: p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
        unit *= 2
    return xs
print(merge_sort(testArr))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
