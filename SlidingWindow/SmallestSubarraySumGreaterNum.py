import sys

def smallestSubarray(arr, k):
    n = len(arr)
    
    window_sum = 0
    start = 0
    end = 0
    min_window_size = sys.maxsize

    for i in range(n):

        while window_sum <= k and end < n:
            window_sum += arr[end]
            end += 1 

        if end-start < min_window_size and window_sum>k:
            min_window_size = end-start
        window_sum -= arr[start]
        start += 1 
    
    return min_window_size


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(smallestSubarray(arr, 21))