"""
Bubble Sorting Algorithm

Run the code and see that BubbleSortB is more time efficient than BubbleSortA
"""

def BubbleSortA(arr):
    iterations = 0
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            iterations+=1
            
    return arr, iterations


def BubbleSortB(arr):
    iterations=0
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            iterations+=1
            
    return arr, iterations
    
arr = [5, 1, 4, 2, 6, 8, 3, 7, 9] #9 element
# arr = int(input())

sortedarrA, interations = BubbleSortA(arr)
print("InterationsA = {}\nsortedarrA = {}".format(interations, sortedarrA))
sortedarrB, interations = BubbleSortB(arr)
print("InterationsB = {}\nsortedarrB = {}".format(interations, sortedarrB))
