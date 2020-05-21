"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, l, r):
    if l < r:
        pivot = r
        i = l
        while i < pivot:
            if array[pivot] < array[i]:
                if pivot == i+1:
                    array[i], array[pivot] = array[pivot], array[i]
                else:
                    array[pivot], array[pivot-1] = array[pivot-1], array[pivot]
                    array[i], array[pivot] = array[pivot], array[i]
                pivot = pivot - 1
            else:
                i+=1
        quicksort(array, l, pivot-1) #left partition
        quicksort(array, pivot+1, r) #right partition

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
l = 0
r = len(test)-1
print quicksort(test, l, r)
