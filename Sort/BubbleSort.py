def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
        if swapped == False:
            break
    

arr = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(arr)
print(arr)