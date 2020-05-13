def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        arr_left = arr[:mid]
        arr_right = arr[mid:]
        
        mergeSort(arr_left)
        mergeSort(arr_right)
        
        i = 0 #i for left
        j = 0 #j for right
        
        k = 0#k for main array
        
        while not(i == len(arr_left) and j == len(arr_right)):
            if j == len(arr_right):
                arr[k] = arr_left[i]
                i+=1
            elif i == len(arr_left):
                arr[k] = arr_right[j]
                j+=1
            else:
                if arr_left[i] < arr_right[j]:
                    arr[k] = arr_left[i]
                    i+=1
                else:
                    arr[k] = arr_right[j]
                    j+=1
            k+=1
        print(arr)
    return arr
    

arr = [8, 7, 6, 5, 4, 3, 2, 1]
print("original arr = ", arr)
sorted_arr = mergeSort(arr)
print("sorted_arr = ", sorted_arr)
