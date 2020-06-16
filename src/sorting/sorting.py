# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i += 1
        else:
            result.append(arrB[j])
            j += 1
    result += arrA[i:]
    result += arrB[j:]

    return result

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    left = arr[:midpoint]
    right = arr[midpoint:]

    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([1, 5, 4, 2, 8, 4, 7, 6]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
