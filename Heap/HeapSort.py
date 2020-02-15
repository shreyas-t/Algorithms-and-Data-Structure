import math

def heapSort(arr):

    n = len(arr)

    if n == 0:
        return

    i = math.floor(n/2) -1

    while i >= 0:
        heapify(arr, i, n)
        i -= 1
    
    print(arr)
    
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def heapify(arr, i, n):

    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)




arr = [11, 10, 8, 6, 7, 8, 5, 5, 3, 6, 7, 7, 6, 3, 1, 1, 1, 1, 2, 5, 2, 2, 4, 3, 4, 5, 2]
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i],end=' ') 