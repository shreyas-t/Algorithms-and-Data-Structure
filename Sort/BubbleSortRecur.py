def bubbleSort(arr, n):
    if n <= 1:
        return 

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubbleSort(arr, n-1)    

arr = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(arr, len(arr))
print(arr)