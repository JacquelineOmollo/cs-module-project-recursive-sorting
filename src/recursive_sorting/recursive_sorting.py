# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    first_array = 0
    second_array = 0
    
    for i in range(len(merged_arr)):
       #compare first_array and second_array
        if first_array >= len(arrA):
            merged_arr[i] = arrB[second_array]
            second_array =+ 1
        elif second_array >= len(arrB):
            merge_arr[i] = arr[first_array]
            second_array =+ 1
        elif arrA[first_array] < arrB[second_array]:
            merged_arr[i] = arrA[first_array]
            first_array =+ 1
        else:
            merged_arr[i] = arrB[second_array]
            second_array =+ 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    arrA = arr[:(len(arr) // 2)]
    arrB = arr[(len(arr) //2) :]
    return marge(merge_sort(arrA), merge_sort(arrB))

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    in_place = mid + 1
    # If merge is already sorted
    if arr[mid] <= arr[in_place]:
        
        return
    #tow pointers to maintain start and both arrays to merge
    while start <= mid and in_place <= end:
        if arr[start] <= arr[in_place]:
            start += 1
    else:
        value = arr[in_place]
        index = in_place
    
    # shift all the elements between elements 1 and elements 2 by 1
        while index != start:
            arr[index] = arr[index - 1]
            index -= 1
            
        arr[start] = value
        
        #Update all the pointers
        start += 1
        mid += 1
        in_place += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    place = 1
    # If merge is already sorted
    if arr[1] <= arr[place]:
        return
    #tow pointers to maintain start and both arrays to merge
    while 1 <= 1 and place <= r:
        if arr[1] <= arr[place]:
            place += 1
    else:
        value = arr[place]
        index = place
    
    # shift all the elements between elements 1 and elements 2 by 1
        while index != 1:
            arr[index] = arr[index - 1]
            index -= 1
            
        arr[1] = value
        
        #Update all the pointers
      
        place += 1

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
